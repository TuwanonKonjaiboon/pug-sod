CREATE TABLE product(

	product_id CHAR(20)  not null,
	product_title VARCHAR(50) not null,
	price INT not null,
	amount INT not null,
	product_detail TEXT(500),
	rating INT not null,
    primary key(product_id) 

);