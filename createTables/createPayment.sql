CREATE TABLE payment(
	payment_id int NOT NULL auto_increment,
    customer_id int not null,
    method ENUM('1','2','3') NOT NULL,
    payment_status ENUM('P','S','C') NOT NULL, #pending success canceled
	create_at DATETIME NOT NULL,
    primary key (payment_id)
);