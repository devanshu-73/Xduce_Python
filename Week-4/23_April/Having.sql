use practice;

-- sequence : FROM > WHERE > GROUP BY > HAVING > ORDER BY
-- WHERE clause : filters rows before any grouping or aggregation occurs.
-- HAVING clause : filters groups of rows after they have been grouped and aggregated.

-- Count of People in Each City with More than 30 Years of Age:

select city_name,count(*) as people30
from table1
group by city_name
having avg(age) > 30;

-- List Cities with Average Age Above 35 and More Than 1 Residents:

select city_name, avg(age) as avg_age, count(*) as people35
from table1
group by city_name
having avg_age > 35 and people35 > 1;

select * from table1;


INSERT INTO table1 (id, name, age, city_name)
VALUES
    (27, 'Henry', 29, 'Boston'),
    (28, 'Isabel', 32, 'Denver'),
    (29, 'Jack', 38, 'Atlanta'),
    (30, 'Karen', 27, 'Philadelphia'),
    (31, 'Liam', 33, 'San Diego'),
    (32, 'Mia', 31, 'Dallas'),
    (33, 'Nathan', 41, 'Phoenix'),
    (34, 'Olivia', 26, 'Austin'),
    (35, 'Peter', 36, 'Portland'),
    (36, 'Quinn', 30, 'San Antonio'),
    (37, 'Rachel', 34, 'Las Vegas'),
    (38, 'Samuel', 39, 'Detroit'),
    (39, 'Tara', 28, 'Minneapolis'),
    (40, 'Uma', 37, 'Orlando'),
    (41, 'Victor', 43, 'Salt Lake City'),
    (42, 'Wendy', 35, 'Kansas City'),
    (43, 'Xavier', 42, 'Tampa'),
    (44, 'Yvonne', 29, 'St. Louis'),
    (45, 'Zachary', 32, 'Sacramento'),
    (46, 'Alice', 31, 'San Jose'),
    (47, 'Bob', 37, 'Seattle'),
    (48, 'Charlie', 39, 'Houston'),
    (49, 'David', 26, 'Chicago'),
    (50, 'Eve', 24, 'Los Angeles');