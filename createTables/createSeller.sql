CREATE TABLE seller(
	seller_id int  NOT NULL,
    seller_description varchar(300),
    is_active boolean NOT NULL,
    certification boolean NOT NULL,
    primary key(seller_id)
);