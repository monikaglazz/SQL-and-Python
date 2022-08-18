CREATE DATABASE shop;
USE shop;

CREATE TABLE IF NOT EXISTS couriers (
	id INT NOT NULL,
    courierName VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    ifAvaible TINYINT NOT NULL,
    howManyParcels INT,
    PRIMARY KEY(id)
);

TRUNCATE TABLE couriers;
INSERT INTO couriers (id, courierName, city, ifAvaible, howManyParcels) 
	VALUES ('123', 'Piter', 'Warsaw', '0', '3'),
    ('176', 'Marcin', 'Warsaw', '0', '1'),
    ('234', 'Artur', 'Wroclaw', '1', 'NULL'),
    ('235', 'Alicia', 'Warsaw', '0', '7'),
    ('456', 'Mario', 'Leszno', '0', '5'),
    ('555', 'Lech', 'Cracow', '1', 'NULL'),
    ('612', 'Piter', 'Katowice', '1', 'NULL');
    
CREATE TABLE IF NOT EXISTS orders (
	id INT NOT NULL,
    howManyProducts INT NOT NULL,
    val FLOAT NOT NULL,
    ifPaid TINYINT NOT NULL,
    PRIMARY KEY(id)
);

TRUNCATE TABLE orders;
INSERT INTO orders (id, howManyProducts, val, ifPaid)
	VALUES ('14', '3', '35.47', '1'),
    ('19', '2', '89,98', '1'),
    ('22', '9', '143.56', '0'),
    ('23', '12', '234.00', '1'),
    ('28', '1', '19.99', '0');
    
CREATE TABLE IF NOT EXISTS parcels (
	id INT NOT NULL,
    orderID INT NOT NULL,
    shipmentDate DATE NOT NULL,
    orderDate DATE,
    PRIMARY KEY (id),
    FOREIGN KEY(orderID) REFERENCES orders(id)
);

INSERT INTO parcels (id, orderID, shippmentDate, orderDate)
	VALUES ('1234', '14', '2021-03-31', '2021-04-08'),
    ('2345', '19', '2021-04-05', 'NULL'),
	('5678', '23', '2021-04-21', '2021-04-26');

