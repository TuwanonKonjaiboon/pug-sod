SELECT S.seller_id,S.shop_name,MAX(cus_num) FROM seller as S INNER JOIN 
(SELECT P1.seller_id,COUNT(DISTINCT O1.customer_id) as cus_num  FROM 
orderItem O1 INNER JOIN product P1 ON O1.product_id = P1.product_id
WHERE O1.customer_id IN  
(SELECT customer_id FROM orderItem O 
INNER JOIN product P on O.product_id = P.product_id AND seller_id = 1) && P1.seller_id != 1
GROUP BY P1.seller_id) 
AS common ON S.seller_id = common.seller_id;