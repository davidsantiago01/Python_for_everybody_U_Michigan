-- Select Information: select statement retrieves a group of records - youcan either retrieve all the records or a subset of the records with a WHERE clause
select * from users
select name from users

-- SQL Insert: Insert statements inserts a row into a table
insert into users (name, email)
values ("Pete", "Pete@umichigan.com";

-- SQL Delete: Deletes a row in a table based on a selection critera
delete from users where email="Pete@umichigan.com"

-- SQL Update: allows the updating of a field with a where clause
update users Set name = "Charles" where email = "csev@umichigan.com"

-- Sorting with ORDER BY: you can add an order by clause to select statements to get the results sorted in ascending or descending order
select * from users order by email
select * from users order by name 
