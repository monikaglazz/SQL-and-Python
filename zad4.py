import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', password = '}oW_z?Pz6;66', host = 'localhost', database='Sales')

    print("Enter the data for new order")

    x = True
    while x:
        try:
            order_number = int(input("Order number: "))
            if len(str(order_number)) != 4:
                print("Wrong order number. Order number must have 4 digits.")
                continue
            elif order_number <= 0:
                print("Order number cannot be negative number!")
                continue
            else:
                cursor = cnx.cursor()
                order_number_tuple = (order_number,)
                existance = ("SELECT recipient FROM Orders WHERE orderID = %s")
                cursor.execute(existance, order_number_tuple)
                result = cursor.fetchall()
                if len(result) != 0:
                    print("Such an order already exists.")
                    continue
                else:
                    x = False
        except ValueError:
            print("Wrong order number. Order number must have 4 digits.")

    z = True
    while z:
        product_name = input("Product name: ")
        if product_name == "":
            print("Product name cannot be empty!")
            continue
        else:
            z = False

    y = True
    while y:
        try:

            quantity = int(input("Quantity of product: "))
            if quantity == "":
                print("Quantity cannot be empty!")
                continue
            elif int(quantity) <= 0:
                print("Quantity cannot be a negative number neither zero")
                continue
            else:
                y = False
        except ValueError:
            print("Wrong quantity. It has to be integer number and cannot be negative nuber.")

    cursor = cnx.cursor()
    product_name_tuple = (product_name,)
    product_quantity_tuple = (quantity,)
    query1 = ("SELECT productID FROM Products WHERE productName = %s")
    query2 = ("SELECT stock FROM Products WHERE productID = %s")
    query3 = ("SELECT SUM(quantity) FROM OrdersProducts WHERE productNumber = %s")

    cursor.execute(query1, product_name_tuple)
    result = cursor.fetchone()
    if result is None: # len(result) == 0:
        print("Product not found.")
    else:
        id = result[0]
        cursor.execute(query2, result)
        result2 = cursor.fetchone()
        cursor.execute(query3, result)
        result3 = cursor.fetchone()

        stock1 = result2[0]
        quantity1 = result3[0]

        print("Stock of {} is: {} ".format(product_name, stock1))
        if quantity1 is None:
            print("Product hasn't been ordered yet: {}".format(product_name))
        else:
            print("Quantity of already ordered product: {} ".format(quantity1))

        current_stock = 0
        if quantity1 is None:
            current_stock = int(stock1)
            quantity1 = 0
        else:
            current_stock = int(stock1) - int(quantity1)

        if int(current_stock) < int(quantity):
            print("Current stock isn't enough for placing order")
            cursor.close()
            cnx.close()
        else:
            print("Current stock is enough for placing order")
            recipient = input("Recipient data: ")
            add_order = ("INSERT INTO Orders (orderID, recipient) VALUES (%s, %s)")
            add_order_product = ("INSERT INTO OrdersProducts VALUES (%s, %s, %s)")

            data = (order_number, recipient)
            cursor.execute(add_order, data)
            print("Order added to Orders table")
            cursor.execute(add_order_product, (order_number, id, quantity))
            print("Order added to OrdersProducts table")
            cnx.commit()
            cursor.close()
            cnx.close()

except mysql.connector.Error:
    print("Wrong database data. Try again :( ")
