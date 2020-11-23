CREATE DEFINER=`root`@`localhost` PROCEDURE `addToCart`(
    c_id integer,
    p_id integer,
    o_id integer,
    qtt integer)
BEGIN
	IF EXISTS(SELECT product_id FROM product WHERE product_id = p_id)
	then
	INSERT INTO orderitem (customer_id,product_id,order_id,quantity)
	VALUES (c_id,p_id,o_id,qtt);

	END IF;
END