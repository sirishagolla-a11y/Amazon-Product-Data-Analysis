-- Q1: Top 5 Highest Rated Products

SELECT product_name, rating
FROM amazon_products
ORDER BY rating DESC
LIMIT 5;  

-- Q2: Top 5 Products With Highest Discounts

SELECT product_name, discount_percentage
FROM amazon_products
ORDER BY discount_percentage DESC
LIMIT 5;

-- Q3: Top 5 Most Reviewed Products

SELECT product_name, rating_count
FROM amazon_products
ORDER BY rating_count DESC
LIMIT 5;

-- Q3: Top 5 Most Reviewed Products

SELECT product_name, rating_count
FROM amazon_products
ORDER BY rating_count DESC
LIMIT 5;

-- Q4: Average Product Rating by Category

SELECT category, AVG(rating) AS average_rating
FROM amazon_products
GROUP BY category
ORDER BY average_rating DESC
LIMIT 10;

-- Q5: Top 5 Most Expensive Products

SELECT product_name, actual_price
FROM amazon_products
ORDER BY actual_price DESC
LIMIT 5;

-- Q6: Low Rated Products With High Discounts

SELECT product_name, rating, discount_percentage
FROM amazon_products
WHERE rating < 3.5
AND discount_percentage > 50
ORDER BY discount_percentage DESC;

-- Q7: Number of Products in Each Category

SELECT category, COUNT(*) AS product_count
FROM amazon_products
GROUP BY category
ORDER BY product_count DESC
LIMIT 10;