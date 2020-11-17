CREATE TABLE ordert(

	order_id int(20),
    create_at datetime,
    order_status ENUM('W','C','P','S','A'), #waiting,confirmed,paid,sent,arrived
    shipping_charge int ,
    total_price int,
    discount int,
	
    primary key(order_id)
);