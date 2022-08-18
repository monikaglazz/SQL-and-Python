USE shop;

CREATE TABLE IF NOT EXISTS returned (
    returnedID INT NOT NULL AUTO_INCREMENT,
    returnedDate DATE NOT NULL,
    orderID INT NOT NULL,
    parcelID INT NOT NULL,
    returnedMoney FLOAT,
    PRIMARY KEY(returnedID),
    FOREIGN KEY(orderID) REFERENCES orders(id),
    FOREIGN KEY(parcelID) REFERENCES parcels(id)
);

TRUNCATE TABLE returned;
INSERT INTO returned
	(returnedID, orderID, parcelID, returnedMoney)
VALUES
	('2021-04-23','14', '1234', NULL),
    ('2021-04-30','19', '2345', '60.55');  
