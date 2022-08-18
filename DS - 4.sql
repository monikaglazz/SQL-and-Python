USE shop;

SELECT orders.id, parcels.shipmentDate FROM orders INNER JOIN parcels ON orders.id = parcels.orderID;
SELECT parcels.id, orders.val, orders.howManyProducts FROM parcels LEFT JOIN orders ON orders.id = parcels.orderID;
