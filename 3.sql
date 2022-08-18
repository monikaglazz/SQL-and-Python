USE shop;

SELECT MIN(val), MAX(val) FROM orders; 
SELECT AVG(howManyProducts) FROM orders;
SELECT SUM(howManyProducts) FROM orders;
SELECT COUNT(id), ifPaid FROM orders GROUP BY ifPaid;