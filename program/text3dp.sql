CREATE DATABASE `text3db`;
SHOW DATABASES;
USE `text3db`;

CREATE TABLE `measure`(
	`mea_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `birth_date` DATE,
    `sex` VARCHAR(1),
    `mea_value` INT,
    `mea_date` DATE
);

DROP TABLE `measure`;
