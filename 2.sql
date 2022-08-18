USE shop;

INSERT INTO couriers VALUES ('472', 'Marta', 'Chorzow', '0', '4');
UPDATE couriers SET ifAvaible='1', howManyParcels=NULL WHERE id='176';
SET SQL_SAFE_UPDATES = 0;
DELETE FROM couriers WHERE city='Warsaw';