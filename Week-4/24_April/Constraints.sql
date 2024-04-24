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
physics_marks int,
maths_marks int,
chemistry_marks int);

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

select s_name,sum(physics_marks+maths_marks+chemistry_marks) as Total_Marks,(sum(physics_marks+maths_marks+chemistry_marks)/3) as Result
from student
group by s_name
order by result desc;


select * from student;