CREATE TABLE promotion(
	promotion_id int NOT NULL,
    seller_id int NOT NULL,
	promotion_title VARCHAR(20) NOT NULL,
    promotion_description VARCHAR(300),
	discount_amount int NOT NULL,
	min_spent INT NOT NULL,
	primary key(promotion_id)
)