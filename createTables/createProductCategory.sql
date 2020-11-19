CREATE TABLE product_category(
	product_id int  NOT NULL,
    category_id int NOT NULL,
    primary key(product_id,category_id)
);