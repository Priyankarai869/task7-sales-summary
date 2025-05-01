#Step 1:  Creating Database
create database sales_db;
use sales_db;

#Step2 Creating table
create table sales(id int auto_increment primary key,product varchar(100),quantity int, price decimal(10,2));

#Step 3: Inserting values in the table of sales
insert into sales (product,quantity,price) values 
('Laptop', 5, 70000),
('Phone', 10, 30000),
('Tablet', 7, 25000),
('Laptop', 3, 70000),
('Phone', 5, 30000);