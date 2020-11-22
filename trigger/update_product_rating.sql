DELIMITER //
CREATE TRIGGER update_product_rating
AFTER INSERT ON review
FOR EACH ROW
BEGIN
	UPDATE product
	SET avg_rating =
		(SELECT AVG(rating)
		FROM review R
		WHERE product_id = new.product_id)
	WHERE product_id = new.product_id;
END //

DELIMITER ;