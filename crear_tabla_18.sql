drop database if EXISTS tiempo;

create database tiempo charset latin1 collate latin1_spanish_ci;

use tiempo;

create table verano (`fecha` DATE PRIMARY KEY, `dia` VARCHAR(15), `alcorcon` FLOAT, `mostoles` FLOAT, `leganes` FLOAT, `fuenlabrada` FLOAT, `getafe` FLOAT, `temp_media` FLOAT, `clasificacion` VARCHAR(10));


LOAD DATA INFILE "C:/ejemplos/ejercicio_18/ejercicio18.csv" INTO TABLE verano
		FIELDS TERMINATED BY  ';'			
		LINES TERMINATED BY '\n'
