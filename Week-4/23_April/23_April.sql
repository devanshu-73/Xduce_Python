use sakila;

select * from film_category;
-- --------------------------------------------------------
-- Distinct

select distinct category_id from film_category;
-- --------------------------------------------------------
-- Joins

-- Inner Join : U can write simply 'JOIN' or 'table1 INNER JOIN table2'
select film.film_id,film.title,film_category.category_id from film inner join film_category on film.film_id = film_category.film_id;

-- Left (Outer) Join : 'table1 LEFT JOIN table2'
select film.film_id,film.title,film_category.category_id from film left join film_category on film.film_id = film_category.film_id;

-- Right (Outer) Join : 'table1 RIGHT JOIN table2'
select film.film_id,film.title,film_category.category_id from film right join film_category on film.film_id = film_category.film_id;

-- Full (Outer) Join : 'table1 FULL JOIN table2'
select * from actor full join film_actor on  actor.actor_id = film_actor.actor_id;

-- --------------------------------------------------------
-- Count

select count(film_category.category_id) from film join film_category where film.film_id = film_category.film_id;
-- --------------------------------------------------------

