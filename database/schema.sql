
CREATE DATABASE astronomical_archive;
USE astronomical_archive;

CREATE TABLE images(
	image_id INT AUTO_INCREMENT PRIMARY KEY,
    object_name VARCHAR(100) NOT NULL,
    observation_date DATE NOT NULL,
    observation_time TIME,
    telescope_id INT,
    instrument_id INT,
    observer_id INT,
    filter_id INT,
    exposure_time DECIMAL(8,2),
    ra DECIMAL(10,6),
    dec_coord DECIMAL(10,6),
    file_path VARCHAR(255) NOT NULL,
    thumbnail_path VARCHAR(255),
    image_format ENUM('FITS','PNG','JPG','JPEG','TIFF'),
    image_size_mb DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 );
 
 CREATE TABLE telescopes(
 telescope_id INT AUTO_INCREMENT PRIMARY KEY,
 telescope_name VARCHAR(100) NOT NULL,
 observatory VARCHAR(150),
 location VARCHAR(150),
 aperture DECIMAL(5,2),
 status ENUM("ACTIVE","INACTIVE")
 );

CREATE TABLE instruments(
instrument_id INT AUTO_INCREMENT PRIMARY KEY,
instrument_name VARCHAR(100),
instrument_type VARCHAR(100),
resolution VARCHAR(50),
wavelength_range VARCHAR(100)
);

CREATE TABLE observers(
observer_id INT AUTO_INCREMENT PRIMARY KEY,
observer_name VARCHAR(100),
department VARCHAR(100),
email VARCHAR(150),
designation VARCHAR(100)
);

CREATE TABLE filters(
filter_id INT AUTO_INCREMENT PRIMARY KEY,
filter_name VARCHAR(50),
wavelength_nm INT,
description TEXT
);

ALTER TABLE images ADD CONSTRAINT fk_telescope FOREIGN KEY (telescope_id) REFERENCES telescopes(telescope_id) ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE images ADD CONSTRAINT fk_instrument FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)  ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE images ADD CONSTRAINT fk_observer FOREIGN KEY (observer_id) REFERENCES observers(observer_id)  ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE images ADD CONSTRAINT fk_filter FOREIGN KEY (filter_id) REFERENCES filters(filter_id) ON DELETE SET NULL ON UPDATE CASCADE;
