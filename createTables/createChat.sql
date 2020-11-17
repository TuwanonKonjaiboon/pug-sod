CREATE TABLE chat(
	customer_id CHAR(20) NOT NULL,
	seller_id CHAR(20) NOT NULL,
	chat_timestamp TIMESTAMP NOT NULL,
	message TEXT(200) NOT NULL,
	sender ENUM('seller', 'customer') NOT NULL,
	primary key (customer_id, seller_id, chat_timestamp)
);