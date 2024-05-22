-- use DETAILS;

-- Single Column Indexes Or Simple Indexes

create index index_single_col
on student_details(name);

-- Multiple Column Indexes Or Composite Indexes
create index index_multi_col
on student_details(name,age);