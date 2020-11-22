DELIMITER $$

CREATE FUNCTION TopProduct()
RETURNS varchar(20)
DETERMINISTIC

BEGIN 
	DECLARE top_product varchar(20);
    
	SET top_product = (SELECT P.product_title FROM orderItem O NATURAL JOIN product P 
    GROUP BY O.product_id ORDER BY SUM(quantity) DESC LIMIT 0,1);
    
    RETURN (top_product);
END; 



