CREATE TABLE category(

	product_id CHAR(20) NOT NULL,
	category_title VARCHAR(20) NOT NULL,
    primary key(category_title),
    foreign key(product_id) references product(product_id) on delete cascade 

);