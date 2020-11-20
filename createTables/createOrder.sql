CREATE TABLE ordert(

	order_id int not null auto_increment,
    order_status ENUM('W','C','P','S','A'), #waiting,confirmed,paid,sent,arrived
    payment_id int,
    tracking_number varchar(20),
    total_price int not null,
    shipping_charge int not null,
    discount int not null,
    create_at datetime not null,
	
    primary key(order_id)
);