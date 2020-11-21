DELIMITER $$

CREATE FUNCTION TopProduct()
RETURNS varchar(20)
DETERMINISTIC

BEGIN 
	DECLARE top_product varchar(20);
    
	SET top_product = (SELECT P1.product_title FROM product P1 ,
    (SELECT product_id, SUM(quantity) as total
	FROM orderItem GROUP BY product_id ORDER BY total DESC LIMIT 0,1) AS top WHERE P1.product_id = top.product_id);
    
    RETURN (top_product);
END; 



