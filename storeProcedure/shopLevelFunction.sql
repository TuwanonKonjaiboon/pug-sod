DELIMITER $$ 
CREATE FUNCTION ShopLevel(sid int)
RETURNS VARCHAR(20)
DETERMINISTIC 
BEGIN
	
    DECLARE avg_rating double;
    DECLARE lvl varchar(20);
    
	SET avg_rating = (SELECT avg(rating) FROM review NATURAL JOIN product WHERE seller_id = sid);
    IF avg_rating > 4 THEN SET lvl = 'good';
    ELSEIF avg_rating > 3 THEN SET lvl = 'fair';
    ELSEIF avg_rating > 2 THEN SET lvl = 'risky';
    ELSEIF avg_rating > 1 THEN SET lvl = 'terrible'; 
    END IF;
    

    RETURN(lvl);
END $$


