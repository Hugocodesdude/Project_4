DROP DATABASE IF EXISTS project_4;
CREATE DATABASE project_4;
USE project_4;

SET GLOBAL local_infile=1;

CREATE TABLE trump_rally_speeches (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    location varchar(255),
    dates varchar(255),
    years varchar(255),
    speech Varchar(10000)
    ); 