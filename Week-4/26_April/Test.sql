create database test;

-- Q - 1
create table tblEmployee (
id int auto_increment primary key,
emp_id int not null unique,
first_name varchar(15),
last_name varchar(15),
salary int,
joining_date date,
department varchar(20)
);

-- Q - 2
insert into tblEmployee (emp_id,first_name,last_name,salary,joining_date,department)
values 
(1,'Devanshu','Chauhan',2500,'2024-01-01','DTS'),
(2,'Mohsin','Rangrej',2000,'2024-01-02','DTS'),
(3,'Shivam','Jani',4000,'2023-11-03','Admin'),
(4,'Mansi','Bhatt',5000,'2023-01-31','HR'),
(5,'Milind','Soni',3500,'2023-4-16','HR'),
(6,'Shubham','pathak',2500,'2023-05-01','DTS'),
(7,'jahir','bhatti',2000,'2023-06-01','DTS'),
(8,'harsh','prajapati',4000,'2024-01-01','Admin'),
(9,'sunil','parmar',5000,'2021-05-01','HR'),
(10,'dipika','rathod',3500,'2022-02-01','admin'),
(11,'janvi','gupta',3200,'2023-01-01','HR'),
(12,'shivani','agarwal',4500,'2024-03-17','HR');

-- Q - 3
select upper(first_name) from tblEmployee;

-- Q - 4
select SUBSTRING(first_name, 1, 3) from tblEmployee;    -- SUBSTRING(string, start, length)

-- Q - 5
select first_name,replace(first_name,'a','A') from tblEmployee;    -- replace(string,'Which','Who')

-- Q - 6
select salary from tblemployee where salary >= 5000 and salary <= 10000;

-- Q - 7
create table colne_emp_postion like emp_postion;
select * from colne_emp_postion;

-- Q - 8
select * from tblemployee where first_name like '%a%';

-- Q - 9
select count(*) from tblemployee where department = 'admin';

-- Q - 10
select curdate();

-- Q - 11
select * from tblemployee order by salary desc limit 10;


-- Q -12 
create table clone_emp_postion as select * from emp_postion;
select * from clone_emp_postion;

-- Q - 13

create table emp_postion (
emp_id int not null,
empposition varchar(15),
salary int,
joining_date date
);

insert into emp_postion
values 
(1,'manager',500000,'2024-01-01'),
(2,'executive',75000,'2024-01-02'),
(3,'manager',90000,'2023-11-03'),     -- 500000 , 90000 , 85000 , 75000 , 3500
(4,'lead',85000,'2023-01-31'),
(5,'executive',3500,'2023-4-16');

select * from emp_postion;

select salary from (
select distinct salary from emp_postion order by salary desc limit 2,1
);

-- Q - 14

insert into emp_postion
values 
(1,'manager',500000,'2024-01-01'),
(2,'executive',75000,'2024-01-02'),
(4,'lead',85000,'2023-01-31');

select * from emp_postion;

select *,count(*) occurrences from emp_postion group by emp_id,empposition,salary,joining_date having count(*) > 1;

