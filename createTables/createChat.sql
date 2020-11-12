CREATE TABLE chat(
	customer_id CHAR(20) NOT NULL,
	seller_id CHAR(20) NOT NULL,
	chat_timestamp TIMESTAMP NOT NULL,
	message TEXT(200) NOT NULL,
	sender ENUM('seller', 'customer') NOT NULL,
	primary key (customer_id, seller_id, chat_timestamp),
    foreign key(customer_id) references customer(customer_id) on delete cascade,
    foreign key(seller_id) references seller(seller_id) on delete cascade
);