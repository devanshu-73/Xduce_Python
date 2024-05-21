-- use DETAILS;
create procedure procedure01
as
begin
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'student_details' AND TABLE_SCHEMA = 'dbo')
BEGIN
	create table DBO.student_details (
		name varchar(255) not null,
		age int not null);
	insert into DBO.student_details (name,age) values 
		('Dev',24),('Yash',45),('Sahil',12),('Devanshu',21),('Mohsin',45),('Gaurang',12),
		('Emma', 30),('Liam', 28),('Olivia', 35),('Noah', 19),('Ava', 25),('William', 32),
		('Sophia', 27),('James', 40),('Isabella', 22),('Benjamin', 38),('Mia', 29),('Mason', 33),
		('Charlotte', 26),('Elijah', 31),('Amelia', 24),('Lucas', 37),('Harper', 23),('Alexander', 36),
		('Evelyn', 34),('Michael', 39),('Abigail', 20);
		END
	select * from student_details;
end;

exec procedure01;

drop procedure procedure01;