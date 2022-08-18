CREATE DATABASE sales;
USE sales;

CREATE TABLE IF NOT EXISTS Orders (
    orderID INT NOT NULL,
    recipient VARCHAR(50) NOT NULL,
    PRIMARY KEY(orderID)
);

TRUNCATE TABLE Orders;
INSERT INTO Orders
	(orderID, recipient)
VALUES
	('5632','Piotr Kowalski'),
    ('8648','Marcin Konieczny'),
    ('9464','Agata Kowalska');

CREATE TABLE IF NOT EXISTS Products (
    productID INT NOT NULL,
    productName VARCHAR(50) NOT NULL,
    stock VARCHAR(50) NOT NULL,
    price FLOAT NOT NULL,
    PRIMARY KEY(productID)
);

TRUNCATE TABLE Products;
INSERT INTO Products
	(productID, productName, stock, price)
VALUES
	('5432','Hammer', '34', '2.50'),
    ('9876', 'Drill', '123', '3.45');
    
CREATE TABLE IF NOT EXISTS OrdersProducts (
    orderNumber INT NOT NULL,
    productNumber INT NOT NULL,
    quantity INT NOT NULL,
    CONSTRAINT PK_OrdersProducts PRIMARY KEY (orderNumber, productNumber),
    FOREIGN KEY (orderNumer) REFERENCES Orders (orderID),
    FOREIGN KEY (productNumber) REFERENCES Products (productID)
);

TRUNCATE TABLE OrdersProducts;
INSERT INTO OrdersProducts
	(orderNumber, productNumber, quantity)
VALUES
	('5632','5432', '3'),
    ('8648', '5432', '12');
