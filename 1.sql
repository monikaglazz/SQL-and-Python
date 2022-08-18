USE shop;

SELECT id, courierName FROM couriers;
SELECT id FROM couriers WHERE city='Wroclaw';
SELECT id FROM couriers WHERE NOT ifAvaible='0' AND NOT city='Wroclaw';
SELECT id, courierName FROM couriers WHERE courierName LIKE 'M%';
SELECT id, city FROM couriers GROUP BY howManyParcels;