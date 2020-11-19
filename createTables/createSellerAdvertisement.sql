CREATE TABLE sellerAdvertisement(
	advertisement_id int not null,
    seller_id int not null,
    content_URL varchar(255) not null,
    primary key(advertisement_id)
);