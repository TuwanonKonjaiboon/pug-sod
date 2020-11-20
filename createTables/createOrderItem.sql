CREATE TABLE orderItem(
	orderItem_id int not null auto_increment,
	customer_id int not null,
	product_id int not null,
	order_id int,
	quantity int not null,
    
    primary key(orderItem_id)
);