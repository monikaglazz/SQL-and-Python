CREATE DATABASE sprzedaz;
USE sprzedaz;

CREATE TABLE IF NOT EXISTS Zamowienia (
    IdZamowienia INT NOT NULL,
    Odbiorca VARCHAR(50) NOT NULL,
    PRIMARY KEY(IdZamowienia)
);

TRUNCATE TABLE Zamowienia;
INSERT INTO Zamowienia
	(IdZamowienia, Odbiorca)
VALUES
	('5632','Piotr Kowalski'),
    ('8648','Marcin Konieczny'),
    ('9464','Agata Kowalska');

CREATE TABLE IF NOT EXISTS Produkty (
    IdProduktu INT NOT NULL,
    Nazwa VARCHAR(50) NOT NULL,
    StanMagazynowy VARCHAR(50) NOT NULL,
    CenaJednostkowa FLOAT NOT NULL,
    PRIMARY KEY(IdProduktu)
);

TRUNCATE TABLE Produkty;
INSERT INTO Produkty
	(IdProduktu, Nazwa, StanMagazynowy, CenaJednostkowa)
VALUES
	('5432','Nakretki', '34', '2.50'),
    ('9876', 'Sruby', '123', '3.45');
    
CREATE TABLE IF NOT EXISTS ZamowieniaProdukty (
    NrZamowienia INT NOT NULL,
    NrProduktu INT NOT NULL,
    Ilosc INT NOT NULL,
    CONSTRAINT PK_ZamowieniaProdukty PRIMARY KEY (NrZamowienia, NrProduktu),
    FOREIGN KEY (NrZamowienia) REFERENCES Zamowienia (IdZamowienia),
    FOREIGN KEY (NrProduktu) REFERENCES Produkty (IdProduktu)
);

TRUNCATE TABLE ZamowieniaProdukty;
INSERT INTO ZamowieniaProdukty
	(NrZamowienia, NrProduktu, Ilosc)
VALUES
	('5632','5432', '3'),
    ('8648', '5432', '12');
