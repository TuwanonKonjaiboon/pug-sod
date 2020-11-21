DELIMITER $$

CREATE FUNCTION TopSellShop()
RETURNS varchar(20)
DETERMINISTIC

BEGIN 
	DECLARE top_sell_shop varchar(20);
    
	SET top_sell_shop = (SELECT S1.shop_name FROM seller S1 ,
    (SELECT S.shop_name, P.seller_id,SUM(O.total_price) as total 
	FROM product P NATURAL JOIN orderitem T NATURAL JOIN ordert O NATURAL JOIN seller S
	GROUP BY P.seller_id ORDER BY total DESC limit 0,1) AS top WHERE S1.shop_name = top.shop_name);
    
    RETURN (top_sell_shop);
END;