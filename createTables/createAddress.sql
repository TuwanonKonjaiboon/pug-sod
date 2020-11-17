CREATE TABLE address(
	customer_id int(20) not null,
	house_no varchar(10) not null,
	street varchar(20) ,
	sub_district varchar(20) not null,
	district varchar(20) not null,
	city varchar(20)  not null,
	zipcode INT(5) not null,
    primary key(customer_id)

);