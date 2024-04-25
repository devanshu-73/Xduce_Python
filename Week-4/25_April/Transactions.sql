start transaction;
-- =====================================================================
create database Transactions;
use transactions;

create table CRS (
id int auto_increment primary key,
f_name varchar(10) not null,
age int);

insert into CRS (f_name,age)
values 
('Krishna', 15),
('Raj'  , 26),
('Ramya', 37),
('Mac'  , 48);

savepoint firstCommit;

insert into CRS (f_name,age)
values 
('Dev', 11),
('Anshu', 22),
('Yash', 33),
('Sahil', 44);

savepoint secondCommit;

rollback to firstCommit;
rollback to secondCommit;
-- =====================================================================
set autocommit = 0;

select * from crs;
drop database transactions;
commit;