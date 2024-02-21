-- prepares a MySQL server for the project
-- create the DB, and user 
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
-- hbnb_dev should have all priviledges on database hbnb_dev_db
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
-- hbnb_dev should have SELECT priviledges on database
