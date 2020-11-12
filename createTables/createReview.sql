CREATE TABLE review(
	product_id CHAR(20) not null,
	customer_id CHAR(20) not null,
	rating INT not null,
	review_comment  TEXT(255),
    primary key(product_id, customer_id),
    foreign key(product_id) references product(product_id) on delete cascade,
    foreign key(customer_id) references customer(customer_id) on delete cascade
);