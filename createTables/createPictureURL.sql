CREATE TABLE pictureURL(
	product_id int NOT NULL,
    url varchar(255) NOT NULL,
    primary key(product_id,url)
);