CREATE TABLE review(
	product_id int not null,
	customer_id int not null,
	rating INT not null,
	comment  TEXT(255),
    create_at DATETIME not null,
    primary key(product_id, customer_id)
);