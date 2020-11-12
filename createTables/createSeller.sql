CREATE TABLE seller(
	seller_id  char(20) NOT NULL,
    primary key(seller_id),
    foreign key(seller_id) references user(user_id)
    on delete cascade
);