import mysql.connector
from mysql.connector import errorcode
import sys
import datetime

if len(sys.argv) > 1:
    status = sys.argv[1]

    try:
        cnx = mysql.connector.connect(user='root', password='}oW_z?Pz6;', host='localhost', database='Parcels')
        cursor = cnx.cursor()
        format = "%Y-%m-%d"
        if status == "shipment":
            if len(sys.argv) == 5:
                sender = sys.argv[2]
                date = sys.argv[3]
                city = sys.argv[4]
                try:
                    datetime.datetime.strptime(date, format)
                    add = ("INSERT INTO Parcels (sender, shipmentDate, arrivalCity) VALUES (%s, %s, %s)")
                    data = (sender, date, city)
                    cursor.execute(add, data)
                    cnx.commit()
                    cursor.close()
                    cnx.close()
                    print("Parcel: {}, {}, {} has been added to Parcels table".format(sender, date, city))
                except ValueError:
                    print("Wrong date, it should be in format yyyy-mm-dd")
                except mysql.connector.DatabaseError:
                    print("Wrong data - parcel hasn't been added. Date format is yyyy-mm-dd")
            else:
                print("Wrong numer of data. You have to gave: sender, shipment date (yyyy-mm-dd) and arrival city")

        elif status == "courier":
            if len(sys.argv) == 3:
                try:
                    id = int(sys.argv[2])
                    id_tuple = (id,)
                    city1 = ("SELECT arrivalCity FROM Parcels WHERE parcelID = %s")
                    cursor.execute(city1, id_tuple)
                    city2 = cursor.fetchone()
                    if city2 is None:
                        print("Parcel {} hasn't been found".format(id))
                    else:
                        is_courier_added = ("SELECT courier FROM Parcels WHERE parcelID = %s")
                        cursor.execute(is_courier_added, id_tuple)
                        courier_added = cursor.fetchone()
                        courier_added1 = courier_added[0]
                        if courier_added1 is None:
                            city3 = city2[0]
                            courier = ("SELECT courierID FROM Couriers WHERE city = %s AND ifAvaible = %s")
                            cursor.execute(courier, (city3, 1))
                            courier_availability = cursor.fetchone()
                            if courier_availability is None:
                                print("There is no available couriers for the parcel {}".format(id))
                                cursor.close()
                                cnx.close()
                            else:
                                courier_availability1 = courier_availability[0]
                                assignment = ("UPDATE Parcels SET courier = %s WHERE parcelID = %s")
                                cursor.execute(assignment, (courier_availability1, id))
                                cnx.commit()
                                cursor.close()
                                cnx.close()
                                print("For the parcel {} the courier ID is {}".format(id, courier_availability1))
                        else:
                            print("Courier was not assigned. Parcel {} already has a courier".format(id))
                except ValueError:
                    print("Parcel ID has to be a number")
            else:
                print("Wrong number of data. Enter the mode, then the package ID")

        elif status == "reception":
            if len(sys.argv) == 4:
                try:
                    parcel_id = int(sys.argv[2])
                    parcel_id_tuple = (parcel_id,)
                    receiving_date = sys.argv[3]
                    datetime.datetime.strptime(receiving_date, format)
                    shipment_date_courier = ("SELECT shipmentDate, courier FROM Parcels WHERE parcelID = %s")
                    cursor.execute(shipment_date_courier, parcel_id_tuple)
                    date_courier = cursor.fetchone()
                    if date_courier is None:
                        print("Parcel {} hasn't been found".format(parcel_id))
                        cursor.close()
                        cnx.close()
                    elif date_courier[1] is None:
                        print("Parcel not in delivery, you cannot confirm receiving")
                        cursor.close()
                        cnx.close()
                    elif datetime.datetime.strptime(str(date_courier[0]), format) > datetime.datetime.strptime(
                            receiving_date, format):
                        print("Date of receiving cannot be earlier than shipment date")
                        cursor.close()
                        cnx.close()
                    else:
                        receiving_date1 = ("SELECT receivingDate FROM Parcels WHERE parcelID = %s")
                        cursor.execute(receiving_date1, parcel_id_tuple)
                        receiving_date2 = cursor.fetchone()
                        if receiving_date2 is None:
                            update = ("UPDATE Parcels SET receivingDate = %s WHERE parcelID = %s")
                            cursor.execute(update, (receiving_date, parcel_id))
                            print("Receiving date is updated: {} for parcel {}".format(receiving_date, parcel_id))
                            cnx.commit()
                            cursor.close()
                            cnx.close()
                        else:
                            print(
                                "Cannot update receiving date. Parcel {} is already delivered".format(parcel_id))
                except ValueError:
                    print("Wrong data. Parcel ID has to be integer number and date has to have yyyy-mm-dd format")
            else:
                print("Not enough data. Enter the mode, parcel id and receiving date")

        elif status == "status":
            if len(sys.argv) == 3:
                try:
                    id = int(sys.argv[2])
                except ValueError:
                    print("Parcel id needs to be a number")
                else:
                    data1 = ("SELECT shipmentDate, courier, receivingDate FROM Parcels WHERE parcelID = %s")
                    cursor.execute(data1, (id,))
                    data_result = cursor.fetchone()
                    if data_result is None:
                        print("Parcel {} hasn't been found".format(id))
                        cursor.close()
                        cnx.close()
                    elif data_result[1] is None:
                        print("Parcel has been shipped: {}".format(data_result[0]))
                        cursor.close()
                        cnx.close()
                    elif data_result[1] is not None and data_result[2] is None:
                        print("Parcel {} is in delivery".format(id))
                        cursor.close()
                        cnx.close()
                    elif data_result[2] is not None:
                        print("Parcel delivered {}".format(data_result[2]))
                        cursor.close()
                        cnx.close()
            else:
                print("Not enough data. Enter the mode and parcel id.")

        elif status == "info":
            if len(sys.argv) == 4:
                if sys.argv[2] == "city":
                    city = sys.argv[3]
                    search = (
                        "SELECT parcelID, sender, shipmentDate, courier, receivingDate FROM Parcels WHERE arrivalCity = %s")
                    city1 = (city,)
                    cursor.execute(search, city1)
                    searched = cursor.fetchall()
                    if len(searched) == 0:
                        print("No parcels for city {}".format(city))
                        cursor.close()
                        cnx.close()
                    else:
                        print("Parcels for city {}".format(city))
                        for w in searched:
                            if w[3] is None:
                                print('ID: {}, sender: {}, shipment date: {}, courier: - , receiving date: -'.format(
                                    w[0], w[1], w[2]))
                                cursor.close()
                                cnx.close()
                            elif w[4] is None:
                                print('ID: {}, sender: {}, shipment date: {}, courier: {} , receiving date: -'.format(
                                    w[0], w[1], w[2], w[3]))
                                cursor.close()
                                cnx.close()
                            else:
                                print('ID: {}, sender: {}, shipment date: {}, courier: {} , receiving date: {}'.format(
                                    w[0], w[1], w[2], w[3], w[4]))
                                cursor.close()
                                cnx.close()

                elif sys.argv[2] == "sender":
                    sender = sys.argv[3]
                    search1 = (
                        "SELECT parcelID, shipmentDate, arrivalCity, courier, receivingDate FROM Parcels WHERE sender = %s")
                    sender1 = (sender,)
                    cursor.execute(search1, sender1)
                    searched = cursor.fetchall()
                    if len(searched) == 0:
                        print("No parcels for sender: {}".format(sender))
                        cursor.close()
                        cnx.close()
                    else:
                        print("Parcels for sender {}".format(sender))
                        for n in searched:
                            if n[3] is None:
                                print(
                                    'ID: {}, sender: {}, shipment date: {}, courier: - , receiving date: -'.format(
                                        n[0], n[1], n[2]))
                                cursor.close()
                                cnx.close()
                            elif n[4] is None:
                                print('ID: {}, sender: {}, shipment date: {}, courier: {} , receiving date: -'.format(
                                        n[0], n[1], n[2], n[3]))
                                cursor.close()
                                cnx.close()
                            else:
                                print('ID: {}, sender: {}, shipment date: {}, courier: {} , receiving date: {}'.format(
                                        n[0], n[1], n[2], n[3], n[4]))
                                cursor.close()
                                cnx.close()
                else:
                    print(
                        "Wrong filer. Avaible filters: city, sender, shipment_date (range), receiving_date (range)")

            elif len(sys.argv) == 5:
                if sys.argv[2] == "shipment_date":
                    shipment_date_beginning = sys.argv[3]
                    shipment_date_ending = sys.argv[4]
                    try:
                        datetime.datetime.strptime(shipment_date_beginning, format)
                        datetime.datetime.strptime(shipment_date_ending, format)
                        if datetime.datetime.strptime(shipment_date_beginning, format) < datetime.datetime.strptime(shipment_date_ending, format):
                            search2 = (
                                "SELECT parcelID, sender, shipmentDate, arrivalCity, courier, receivingDate FROM Parcels WHERE shipmentDate BETWEEN %s AND %s")
                            data2 = (shipment_date_beginning, shipment_date_ending)
                            cursor.execute(search2, data2)
                            searched = cursor.fetchall()
                            if len(searched) == 0:
                                print("No parcels for the shipment dates: {} - {}".format(shipment_date_beginning, shipment_date_ending))
                                cursor.close()
                                cnx.close()
                            else:
                                print("Parcels for shipment dates: {}  {}".format(shipment_date_beginning, shipment_date_ending))

                                for d in searched:
                                    if d[4] is None:
                                        print('ID: {}, sender: {}, shipment date: {}, city: {}, courier: - , receiving date: -'.format(
                                                str(d[0]), str(d[1]), str(d[2]), str(d[3])))
                                        cursor.close()
                                        cnx.close()
                                    elif d[5] is None:
                                        print('ID: {}, sender: {}, shipment date: {}, city: {}, courier: {} , receiving date: -'.format(
                                                str(d[0]), str(d[1]), str(d[2]), str(d[3]), str(d[4])))
                                        cursor.close()
                                        cnx.close()
                                    else:
                                        print('ID: {}, sender: {}, shipment date: {}, city: {}, courier: {} , receiving date: {}'.format(
                                                str(d[0]), str(d[1]), str(d[2]), str(d[3]), str(d[4]), str(d[5])))
                                        cursor.close()
                                        cnx.close()
                        else:
                            print("Wrong range of dates. Ending date cannot be earlier than beginning date.")
                    except ValueError:
                        print("Wrong date format. Should be: yyyy-mm-dd ")

                elif sys.argv[2] == "receiving_date":
                    receiving_date_beginning = sys.argv[3]
                    receiving_date_ending = sys.argv[4]
                    try:
                        datetime.datetime.strptime(receiving_date_beginning, format)
                        datetime.datetime.strptime(receiving_date_ending, format)
                        if datetime.datetime.strptime(receiving_date_beginning, format) < datetime.datetime.strptime(receiving_date_ending, format):
                            search3 = (
                                "SELECT parcelID, sender, shipmentDate, arrivalCity, courier, receivingDate FROM Parcels WHERE receivingDate BETWEEN %s AND %s")
                            data3 = (receiving_date_beginning, receiving_date_ending)
                            cursor.execute(search3, data3)
                            searched = cursor.fetchall()
                            if len(searched) == 0:
                                print("No parcels for the receiving dates: {} - {}".format(
                                    receiving_date_beginning, receiving_date_ending))
                                cursor.close()
                                cnx.close()
                            else:
                                print("Parcels for receiving dates: {} - {}".format(receiving_date_beginning, receiving_date_ending))
                                for e in searched:
                                    if e[4] is None:
                                        print(
                                            'ID: {}, sender: {}, shipment date: {}, city: {}, courier: - , receiving date: -'.format(
                                                str(e[0]), str(e[1]), str(e[2]), str(e[3])))
                                        cursor.close()
                                        cnx.close()
                                    elif e[5] is None:
                                        print(
                                            'ID: {}, sender: {}, shipment date: {}, city: {}, courier: {} , receiving date: -'.format(
                                                str(e[0]), str(e[1]), str(e[2]), str(e[3]), str(e[4])))
                                        cursor.close()
                                        cnx.close()
                                    else:
                                        print(
                                            'ID: {}, sender: {}, shipment date: {}, city: {}, courier: {} , receiving date: {}'.format(
                                                str(e[0]), str(e[1]), str(e[2]), str(e[3]), str(e[4]), str(e[5])))
                                        cursor.close()
                                        cnx.close()
                        else:
                            print("Wrong range of dates. Ending date cannot be earlier than beginning date.")
                    except ValueError:
                        print("Wrong date format. Should be: yyyy-mm-dd ")
                else:
                    print("""Wrong filer. Avaible filters: city, sender, shipment_date (range), receiving_date (range)
                    Enter the mode, then filer name, then data""")
            else:
                print("Not enough data. Enter mode and data")
        else:
            print(
                "Wrong mode. Enter mode and data. Avaible modes: shipment, courier, reception, status, info")
    except mysql.connector.Error:
        print("Wrong data about database")
else:
    print("You have to enter the mode. Avaible modes: shipment, courier, reception, status, info")
