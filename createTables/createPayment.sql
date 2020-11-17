CREATE TABLE payment(
	transaction_id varchar(20) NOT NULL,
    payment_status ENUM('P','C','F') NOT NULL, #pending confirmed failed
    method ENUM('1','2','3') NOT NULL,
	create_at DATETIME NOT NULL,
    primary key (transaction_id)
);