CREATE TABLE seller(
	seller_id int  NOT NULL,
    shop_name varchar(20) NOT NULL,
    description varchar(255),
    is_active boolean NOT NULL,
    certification boolean NOT NULL,
    primary key(seller_id)
);