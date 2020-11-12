CREATE TABLE customer(
	customer_id  char(20) NOT NULL,
    primary key(customer_id),
    foreign key(customer_id) references user(user_id)
    on delete cascade
);