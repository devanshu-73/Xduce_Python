use practice;

select * from film_category;
-- --------------------------------------------------------
-- Distinct

select distinct category_id from film_category;
-- --------------------------------------------------------
-- Count

select count(film_category.category_id) from film join film_category where film.film_id = film_category.film_id;
-- --------------------------------------------------------
-- Joins

-- Inner Join : U can write simply 'JOIN' or 'table1 INNER JOIN table2'
select film.film_id,film.title,film_category.category_id from film inner join film_category on film.film_id = film_category.film_id;

-- Left (Outer) Join : 'table1 LEFT JOIN table2'
select film.film_id,film.title,film_category.category_id from film left join film_category on film.film_id = film_category.film_id;

-- Right (Outer) Join : 'table1 RIGHT JOIN table2'
select film.film_id,film.title,film_category.category_id from film right join film_category on film.film_id = film_category.film_id;

-- Full (Outer) Join : 'table1 FULL JOIN table2'
select film.film_id,film.title,film_category.category_id from film full join film_category on film.film_id = film_category.film_id;

-- --------------------------------------------------------

use practice;

CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    dept_name VARCHAR(50)
);

CREATE TABLE departments (
    dept_id INT,
    dept_name VARCHAR(50)
);

-- drop table departments;

INSERT INTO employees VALUES
(1, 'Alice', 'Sales'),
(2, 'Bob', 'Marketing'),
(3, 'Charlie', 'HR');

INSERT INTO departments VALUES
(1, 'Sales'),
(2, 'Marketing'),
(3, 'Finance');

select dept_name from employees;
select dept_name from departments;

Select emp.dept_name from employees emp FULL JOIN 
departments dept on emp.dept_name = dept.dept_name;

SELECT emp_id, emp_name, departments.dept_id, departments.dept_name
FROM employees
FULL JOIN departments ON employees.dept_name = departments.dept_name;

desc departments;
desc employees;