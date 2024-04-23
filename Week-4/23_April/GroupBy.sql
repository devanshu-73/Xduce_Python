use sakila;

-- Group BY : groups rows that have the same values into table rows
-- Get FirstName Of Customers Who Purchased Most and With total Purchased Amount
select c.first_name,sum(p.amount),p.rental_id 
from customer as c 
right join payment as p on c.customer_id = p.customer_id 
group by first_name;
 
-- Number of rentals per customer: Count the number of rentals made by each customer.




-- SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS customer_name, COUNT(r.rental_id) AS num_rentals
-- FROM customer c
-- LEFT JOIN rental r ON c.customer_id = r.customer_id
-- GROUP BY c.customer_id;

-- Film Table
select special_features,count(special_features) from film group by special_features;


-- =========================================================================================================
-- Aggregate Function : 
select MIN(amount) AS Minimum_Amount from payment;
select MAX(amount) AS Maximum_Amount from payment;
select AVG(amount) AS Total_Collection from payment; -- Also U can Get Only 2 digit using ROUND(AVG(amount),2)

 