use practice;

-- SQL constraints: Primary key, foreign key, unique, not null.

-- ====================================================================================================

-- Unique : 
-- 1) all values in a column are different.
-- 2) you can have many UNIQUE constraints per table

-- Not Null ;
-- 1) By default, a column can hold NULL values.
-- 2) column NOT accept NULL values means always contain some value

create table person (
id int unique not null,
first_name varchar(255) not null,
age int );
  
insert into person values 
    (1, 'Liam', 33),
    (2, 'Mia', 31),
    (3, 'Nathan', 41),
    (4, 'Olivia', 26),
    (5, 'Peter', 36),
    (6, 'Quinn', 30),
    (7, 'Rachel', 34),
    (8, 'Samuel', 39),
    (9, 'Tara', 28),
    (10, 'Karen', 27);

-- ====================================================================================================

-- Primary Key : uniquely identifies each record in a table. 
-- Unique + Not Null = Primary Key

create table student (
s_id int primary key,
s_name varchar(255) not null,
physics int,
maths int,
chemistry int);

insert into student values 
    (01, 'Liam', 97, 91, 87), 
    (02, 'Mia', 87, 92, 37), 
    (03, 'Nathan', 77, 93, 47), 
    (04, 'Olivia', 67, 94, 97), 
    (05, 'Peter', 57, 95, 87), 
    (06, 'Quinn', 47, 81, 77), 
    (07, 'Rachel', 37, 82, 67), 
    (08, 'Samuel', 89, 83, 57), 
    (09, 'Tara', 96, 84, 56), 
    (10, 'Karen', 91, 85, 67);

select s_name,
	sum(physics+maths+chemistry) as Total_Marks,
	sum(physics+maths+chemistry)/3 as Result
from student
group by s_name
order by result desc;

select * from student;

-- ====================================================================================================
-- Foreign Key : used to link two tables together.

create table customers (
    customer_id int primary key,
    customer_name varchar(255) not null
);

create table orders (
    order_id int primary key,
    order_date date,
    amount int,
    customer_id int,
    foreign key (customer_id) references customers(customer_id)
);

insert into customers values
    (1, 'John Doe'),
    (2, 'Jane Smith'),
    (3, 'Michael Johnson'),
    (4, 'Emily Brown'),
    (5, 'William Davis'),
    (6, 'Olivia Wilson');

insert into orders values 
    (101, '2024-04-24', 150.00, 1),  -- Order 101 is associated with customer 1 (John Doe)
    (102, '2024-04-25', 200.00, 2),  -- Order 102 is associated with customer 2 (Jane Smith)
    (103, '2024-04-26', 100.00, 3), -- Order 103 is associated with customer 3 (Michael Johnson)
	(104, '2024-04-27', 120.00, 4),  -- Order 104 is associated with customer 4 (Emily Brown)
    (105, '2024-04-28', 180.00, 5),  -- Order 105 is associated with customer 5 (William Davis)
    (106, '2024-04-29', 90.00, 6); 	-- Order 106 is associated with customer 6 (Olivia Wilson)
