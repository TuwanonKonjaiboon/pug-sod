CREATE TABLE promotion(
	promotion_id char(20) NOT NULL,
	promotion_title VARCHAR(20) NOT NULL,
	description INT NOT NULL,
	discount_amount float(24) NOT NULL,
	min_spent INT NOT NULL,
	Description VARCHAR(300),
	primary key(promotion_id)
)