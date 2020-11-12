CREATE TABLE address(
	user_id char(20) not null,
	house_no varchar(10) not null,
	street varchar(20) ,
	sub_district varchar(20) not null,
	district varchar(20) not null,
	city varchar(20)  not null,
	zipcode INT(5) not null,
    primary key(user_id),
    foreign key(user_id) references customer(customer_id) 
    on delete cascade

);