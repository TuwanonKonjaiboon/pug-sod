CREATE TABLE product(

	product_id int  not null auto_increment,
  seller_id int not null,
	product_title VARCHAR(50) not null,
	product_detail TEXT(500),
	price INT not null,
	amount INT not null,
	avg_rating FLOAT(2,1) DEFAULT 0,
  update_at DATETIME not null DEFAULT CURRENT_TIMESTAMP, 
  primary key(product_id) 

);