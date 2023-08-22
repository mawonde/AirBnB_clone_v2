-- Prepares a MySQL server for the hbnb project.

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
USE `hbnb_test_db`;

-- Create the user and grant privileges
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
