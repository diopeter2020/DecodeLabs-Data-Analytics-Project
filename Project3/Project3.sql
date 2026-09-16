

-- What is the total revenue?
SELECT SUM(TotalPrice) AS TotalRevenue
FROM project3;
-- How many unique customers do we have?
SELECT COUNT(DISTINCT CustomerID) AS TotalCustomers
FROM project3;

-- What are the top 5 products by revenue?
SELECT Product, SUM(TotalPrice) AS Revenue
FROM project3
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5;

-- Which ShippingAddress has the highest number of orders?
SELECT ShippingAddress, COUNT(OrderID) AS OrderCount
FROM project3
GROUP BY ShippingAddress
ORDER BY OrderCount DESC
LIMIT 1;

-- What is the order status breakdown?
SELECT OrderStatus, COUNT(OrderID) AS Count, 
       ROUND(COUNT(OrderID) * 100.0 / (SELECT COUNT(*) FROM project3), 2) AS Percentage
FROM project3
GROUP BY OrderStatus;

-- Which PaymentMethod generates the most revenue?
SELECT PaymentMethod, SUM(TotalPrice) AS Revenue
FROM project3
GROUP BY PaymentMethod
ORDER BY Revenue DESC;

-- Do customers who use a CouponCode spend more on average?
SELECT 
    CASE WHEN CouponCode IS NULL OR CouponCode = '' THEN 'No Coupon' ELSE 'Used Coupon' END AS CouponUsage,
    AVG(TotalPrice) AS AvgOrderValue,
    COUNT(OrderID) AS OrderCount
FROM project3
GROUP BY CouponUsage;

-- What are the top 3 ReferralSources by total revenue?
SELECT ReferralSource, SUM(TotalPrice) AS Revenue
FROM project3
GROUP BY ReferralSource
ORDER BY Revenue DESC
LIMIT 7;

-- What is the average ItemsInCart and Quantity per order for each Product?
SELECT Product, 
       AVG(ItemsInCart) AS AvgItemsInCart,
       AVG(Quantity) AS AvgQuantity,
       AVG(UnitPrice) AS AvgUnitPrice
FROM project3
GROUP BY Product
ORDER BY AvgQuantity DESC;


