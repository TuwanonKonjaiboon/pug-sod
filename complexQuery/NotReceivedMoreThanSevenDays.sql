SELECT DISTINCT  B1.customer_id, 
	B1.order_id, 
    B1.dateDiff, 
    SX.shop_Name
FROM seller SX, 
	Product PX,
(
	SELECT customer_id, 
			I1.product_id, 
            A1.dateDiff, 
			A1.order_id
	FROM orderitem I1, 
		(
		SELECT O.order_id,
				O.tracking_number, 
				DATEDIFF(NOW(), P.create_at) AS dateDiff
		FROM ordert O, payment P
		WHERE O.payment_id IS NOT NULL
			AND O.state != 'S'
			AND O.payment_id = P.payment_id  
			AND P.status = 'S'
			AND DATEDIFF(NOW(), P.create_at) > 3
		) A1
	WHERE I1.order_id = A1.order_id
) B1
WHERE SX.seller_id = PX.seller_id 
	AND B1.product_id = PX.product_id
    
    