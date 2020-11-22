CREATE DEFINER=`root`@`localhost` PROCEDURE `Search`(
IN pName VARCHAR(255),
 IN cName VARCHAR(255),
 IN sName VARCHAR(255)
 )
BEGIN
	SELECT P.product_id,
    P.seller_id,
    P.product_title,
    P.product_detail,
    P.price,
    P.amount,
    P.avg_rating,
    S.shop_name,
    C.category_title
    FROM product P, productcategory PC, category C, seller S
    WHERE P.product_title LIKE CONCAT('%',pName, '%') 
		AND C.category_title LIKE CONCAT('%',cName, '%')
        AND S.shop_name LIKE CONCAT('%',sName, '%')
        AND PC.category_id = C.category_id
		AND P.product_id = PC.product_id
        AND S.seller_id = P.seller_id
        GROUP BY P.seller_id;
END