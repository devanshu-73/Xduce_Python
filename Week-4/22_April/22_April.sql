create database practice;
use practice;

-- -------------------------------------------------------------------------
-- Create : To Create Database and Table

create table table1 (id int primary key,
name varchar(255) not null,
age int not null);
-- -------------------------------------------------------------------------
-- Insert : To Add Data in Table

insert into table1 values 
(01,'Dev',24),
(02,'Yash',45),
(03,'Sahil',12);

insert into table1 values 
(04,'Devanshu',21),(05,'Mohsin',45),(06,'Gaurang',12),(07, 'Emma', 30),(08, 'Liam', 28),
(09, 'Olivia', 35),(10, 'Noah', 19),(11, 'Ava', 25),(12, 'William', 32),
(13, 'Sophia', 27),(14, 'James', 40),(15, 'Isabella', 22),(16, 'Benjamin', 38),
(17, 'Mia', 29),(18, 'Mason', 33),(19, 'Charlotte', 26),(20, 'Elijah', 31),
(21, 'Amelia', 24),(22, 'Lucas', 37),(23, 'Harper', 23),(24, 'Alexander', 36),
(25, 'Evelyn', 34),(26, 'Michael', 39),(27, 'Abigail', 20);
-- -------------------------------------------------------------------------
-- Alter : used to add, delete, or modify columns in an existing table.

alter table table1
add city varchar(255) not null;

alter table table1
drop column city;

alter table table1
rename column city to city_name;  -- Rename Column
-- -------------------------------------------------------------------------
-- Update : update whole column with multiple data

update table1
set city =
    case
        WHEN id = 1 THEN 'New York'
        WHEN id = 2 THEN 'Los Angeles'
        WHEN id = 3 THEN 'Chicago'
        WHEN id = 4 THEN 'Houston'
        WHEN id = 5 THEN 'Phoenix'
        WHEN id = 6 THEN 'Philadelphia'
        WHEN id = 7 THEN 'San Antonio'
        WHEN id = 8 THEN 'San Diego'
        WHEN id = 9 THEN 'Dallas'
        WHEN id = 10 THEN 'San Jose'
        WHEN id = 11 THEN 'Austin'
        WHEN id = 12 THEN 'Jacksonville'
        WHEN id = 13 THEN 'Fort Worth'
        WHEN id = 14 THEN 'Columbus'
        WHEN id = 15 THEN 'Charlotte'
        WHEN id = 16 THEN 'San Francisco'
        WHEN id = 17 THEN 'Indianapolis'
        WHEN id = 18 THEN 'Seattle'
        WHEN id = 19 THEN 'Denver'
        WHEN id = 20 THEN 'Washington'
        WHEN id = 21 THEN 'Boston'
        WHEN id = 22 THEN 'El Paso'
        WHEN id = 23 THEN 'Nashville'
        WHEN id = 24 THEN 'Detroit'
        WHEN id = 25 THEN 'Oklahoma City'
        WHEN id = 26 THEN 'Los Angeles'
        WHEN id = 27 THEN 'Memphis'
    END WHERE id IN (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27);
-- -------------------------------------------------------------------------
--  Delete : To delete Purticular Row's Data

delete from table1 where name = 'abigail';
-- -------------------------------------------------------------------------
-- AND , BETWEEN

SELECT * FROM table1 WHERE age >= 20 AND age <= 30;
select * from table1 where age between 20 and 30; -- between includes 20 and 30 also
-- -------------------------------------------------------------------------


