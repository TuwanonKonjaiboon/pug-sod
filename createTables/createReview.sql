CREATE TABLE review(
	product_id CHAR(20) not null,
	customer_id CHAR(20) not null,
	rating INT not null,
	review_comment  TEXT(255),
    primary key(product_id, customer_id)
);