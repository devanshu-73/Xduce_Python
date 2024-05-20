use DETAILS;

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

-- AND , BETWEEN

SELECT * FROM table1 WHERE age >= 20 AND age <= 30;
select * from table1 where age between 20 and 30; -- between includes 20 and 30 also
-- -------------------------------------------------------------------------

-- ==================================================================================================

select * from CLASS;

select * from EMPLOYEES;



-- join

-- Inner Join
select c.SID,e.E_ID,c.SNAME,e.FNAME from CLASS c inner join EMPLOYEES e on c.SID = e.E_ID;

-- Left Join
select c.SID,e.E_ID,c.SNAME,e.FNAME from CLASS c left join EMPLOYEES e on c.SID = e.E_ID;

-- Right Join
select c.SID,e.E_ID,c.SNAME,e.FNAME from CLASS c right join EMPLOYEES e on c.SID = e.E_ID;

-- Full Join
select c.SID,e.E_ID,c.SNAME,e.FNAME from CLASS c full join EMPLOYEES e on c.SID = e.E_ID;


-- Store Procedure

create procedure procedure1
as 
begin
	select * from EMPLOYEES;
end;

exec procedure1;