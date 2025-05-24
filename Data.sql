CREATE TABLE books 
	(
		book_id INT NOT NULL AUTO_INCREMENT,
		title VARCHAR(100),
		author_fname VARCHAR(100),
		author_lname VARCHAR(100),
		released_year INT,
		stock_quantity INT,
		pages INT,
		PRIMARY KEY(book_id)
	);

INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES
('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343);
select char_length(title) from books;
select title from books;
select char_length(title), title from books;
select concat("I love to read", ' ', upper(title), ' !!!') from books;

select left(author_lname, 1) as Last_Name from books;
select substring(author_lname, 1, 1) as New_Last_Name from books;
select trim(both '.' from '.....Shams...');


-- ===========================================================================
select database();
show databases;
use library;
select database();
CREATE TABLE books 
	(
		book_id INT NOT NULL AUTO_INCREMENT,
		title VARCHAR(100),
		author_fname VARCHAR(100),
		author_lname VARCHAR(100),
		released_year INT,
		stock_quantity INT,
		pages INT,
		PRIMARY KEY(book_id)
	);

INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES
('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343);
select * from books;
select author_lname from books;
select distinct author_lname from books;
select title from books where title like '%the%';
select distinct concat(author_lname, ' ', author_fname) as Unique_Full_Name from books;
select * from books;

select book_id, author_fname, author_lname from books order by author_lname;
select book_id, author_fname, author_lname from books order by author_lname asc;
select book_id, author_fname, author_lname from books order by author_lname desc;
select book_id, released_year book_id desc;
select author_fname, author_lname, released_year from booksorder order by author_lname, released_year;
show databases;
use library;

select * from books;
SELECT 
    author_fname, author_lname, released_year
FROM
    books
ORDER BY author_lname , released_year DESC;

select author_fname, author_lname, released_year from books where author_lname like '%da%';
select * from books;
select author_fname, author_lname, released_year from books where author_fname like '____';
select count(author_fname) from books;
select count(DISTINCT author_fname, author_lname, book_id) as New_Name from books;
select count(book_id) from books;
select count(*) from books where title like '%the%';

select count(distinct author_lname, title) from books;
select count(*) from books where author_fname like '____';
show databases;
select database();
select * from books;
select author_lname,count(*) as Written_Books from books group by author_lname order by Written_Books desc;
select released_year, count(*) as Books_Number from books group by released_year order by Books_Number desc;

select title, pages from books where pages = (select max(pages) from books);

select author_fname, author_lname, count(*) from books group by author_fname, author_lname;
select concat(author_fname, ' ', author_lname) as Author, count(*) as Books_Number from books group by Author;

select concat(author_fname, ' ', author_lname) as Author,
min(released_year) as First_Publish,
count(*) as Book_number from books 
group by Author order by Book_number desc;

select concat(author_fname,' ', author_lname) as Full_Name, min(released_year), max(released_year) from books group by Full_Name;

select author_lname,
count(*) as Books_writte,
min(released_year) as Previously_Written,
max(released_year) as New_Written, 
min(pages) as Pages_Count
from books
group by author_lname;
select title from books;
select author_lname, count(*) from books group by author_lname;
select title, author_lname from books where released_year != 2017;
select author_fname, released_year from books;

select author_fname, author_lname 
from books 
where author_fname != 'neil'; 

select concat(author_fname,' ', author_lname) as Full_Name
from books
where concat(author_fname,' ', author_lname) not like 'da%';

select title, author_fname, pages 
from books 
where pages < 500;

select title, author_fname, released_year 
from books 
where released_year <= 1985;

select title, author_fname, released_year, pages from books
where released_year >= 2012
and pages > 200
and title like '%novel%';

SELECT title, pages FROM books
WHERE pages < 200 
OR title LIKE '%stories%';

select author_fname, author_lname, pages, released_year from books
where released_year 
Not between 2004 and 2015;

select cast('9:0:0' as time) as Time;

SELECT * FROM people WHERE birthtime 
BETWEEN CAST('12:00:00' AS TIME) 
AND CAST('16:00:00' AS TIME);

select author_fname, author_lname, pages, released_year from books
where released_year >=2000
and released_year in ('2000', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016')
order by released_year;

select released_year as Book_Publish
from books
where released_year >=2000
and released_year in ('2000', '2002', '2004', '2006', '2008', '2010', '2012', '2014', '2016')
order by released_year;

select author_fname, author_lname, pages, released_year from books
where released_year >=2000
and released_year % 2 = 1
order by released_year;


SELECT 
    author_fname,
    author_lname,
    pages,
    released_year,
    CASE
        WHEN released_year >= 2000 THEN 'Well Printed Books'
        ELSE 'Not Printed Well'
    END AS 'Print_Quality'
FROM
    books;

SELECT 
    title,
    released_year,
    stock_quantity,
    CASE
        WHEN stock_quantity BETWEEN 0 AND 40 THEN '*'
        WHEN stock_quantity BETWEEN 41 AND 80 THEN '**'
        WHEN stock_quantity BETWEEN 81 AND 110 THEN '***'
        ELSE '*****'
    END AS Stock
FROM
    books
ORDER BY Stock ASC;

SELECT author_fname, author_lname,
	CASE
        WHEN COUNT(*) = 1 THEN '1 book'
        ELSE CONCAT(COUNT(*), ' books')
	END AS count
FROM books
WHERE author_lname IS NOT NULL
GROUP BY author_fname, author_lname;
-- =====================================================================
create database shop;
use shop;
show databases;
select database();
use shop;


CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50)
);
 
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_date DATE,
    amount DECIMAL(8,2),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
 
INSERT INTO customers (first_name, last_name, email) 
VALUES ('Boy', 'George', 'george@gmail.com'),
       ('George', 'Michael', 'gm@gmail.com'),
       ('David', 'Bowie', 'david@gmail.com'),
       ('Blue', 'Steele', 'blue@gmail.com'),
       ('Bette', 'Davis', 'bette@aol.com');
       
       
INSERT INTO orders (order_date, amount, customer_id)
VALUES ('2016-02-10', 99.99, 1),
       ('2017-11-11', 35.50, 1),
       ('2014-12-12', 800.67, 2),
       ('2015-01-03', 12.50, 2),
       ('1999-04-11', 450.25, 5);
       
show tables;
select id from customers where last_name = 'George';
select * from orders where customer_id = 1;
select * from customers, orders;
show databases;
select * from customers 
join orders
on orders.customer_id = customers.id;

SELECT c.id, c.first_name, c.last_name, c.email, o.id AS order_id, o.order_date, o.amount
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE c.first_name = 'George' 
  AND c.last_name = 'Michael' 
  AND o.order_date = '2014-12-12';
  
SELECT 
    c.id,
    c.first_name,
    c.last_name,
    c.email,
    o.id,
    o.order_date,
    o.amount,
    o.customer_id
FROM
    customers c
        JOIN
    orders o ON c.id = o.customer_id
ORDER BY o.amount DESC
LIMIT 1;
select * from orders
join customers 
on customers.id = orders.customer_id;

select * from customers
join orders 
on orders.customer_id = customers.id;
drop table orders;
drop tables customers;
show tables;
select * from orders;
create database shops;
select database();
use shops;
CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50)
);
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_date DATE,
    amount DECIMAL(8,2),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT INTO customers (first_name, last_name, email) 
VALUES ('Boy', 'George', 'george@gmail.com'),
       ('George', 'Michael', 'gm@gmail.com'),
       ('David', 'Bowie', 'david@gmail.com'),
       ('Blue', 'Steele', 'blue@gmail.com'),
       ('Bette', 'Davis', 'bette@aol.com');
       
INSERT INTO orders (order_date, amount, customer_id)
VALUES ('2016-02-10', 99.99, 1),
       ('2017-11-11', 35.50, 1),
       ('2014-12-12', 800.67, 2),
       ('2015-01-03', 12.50, 2),
       ('1999-04-11', 450.25, 5);
       
select * from customers
join orders 
on orders.customer_id = customers.id;

select first_name, last_name, order_date, amount from customers
left join orders
on customers.id = orders.customer_id;

select first_name, last_name, ifnull(sum(amount), 0) as Total_Money from customers
left join orders
on customers.id = orders.customer_id
group by first_name, last_name;

-- ==================================================================================================
-- Many to Many
create database tv_series;
use tv_series;
CREATE TABLE reviewers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);
CREATE TABLE series (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    released_year YEAR,
    genre VARCHAR(100)
);
CREATE TABLE reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    rating DECIMAL(2 , 1 ),
    series_id INT,
    reviewer_id INT,
    FOREIGN KEY (series_id)
        REFERENCES series (id),
    FOREIGN KEY (reviewer_id)
        REFERENCES reviewers (id)
);
INSERT INTO series (title, released_year, genre) VALUES
    ('Archer', 2009, 'Animation'),
    ('Arrested Development', 2003, 'Comedy'),
    ("Bob's Burgers", 2011, 'Animation'),
    ('Bojack Horseman', 2014, 'Animation'),
    ("Breaking Bad", 2008, 'Drama'),
    ('Curb Your Enthusiasm', 2000, 'Comedy'),
    ("Fargo", 2014, 'Drama'),
    ('Freaks and Geeks', 1999, 'Comedy'),
    ('General Hospital', 1963, 'Drama'),
    ('Halt and Catch Fire', 2014, 'Drama'),
    ('Malcolm In The Middle', 2000, 'Comedy'),
    ('Pushing Daisies', 2007, 'Comedy'),
    ('Seinfeld', 1989, 'Comedy'),
    ('Stranger Things', 2016, 'Drama');

INSERT INTO reviewers (first_name, last_name) VALUES
    ('Thomas', 'Stoneman'),
    ('Wyatt', 'Skaggs'),
    ('Kimbra', 'Masters'),
    ('Domingo', 'Cortes'),
    ('Colt', 'Steele'),
    ('Pinkie', 'Petit'),
    ('Marlon', 'Crafford');

INSERT INTO reviews(series_id, reviewer_id, rating) VALUES
    (1,1,8.0),(1,2,7.5),(1,3,8.5),(1,4,7.7),(1,5,8.9),
    (2,1,8.1),(2,4,6.0),(2,3,8.0),(2,6,8.4),(2,5,9.9),
    (3,1,7.0),(3,6,7.5),(3,4,8.0),(3,3,7.1),(3,5,8.0),
    (4,1,7.5),(4,3,7.8),(4,4,8.3),(4,2,7.6),(4,5,8.5),
    (5,1,9.5),(5,3,9.0),(5,4,9.1),(5,2,9.3),(5,5,9.9),
    (6,2,6.5),(6,3,7.8),(6,4,8.8),(6,2,8.4),(6,5,9.1),
    (7,2,9.1),(7,5,9.7),
    (8,4,8.5),(8,2,7.8),(8,6,8.8),(8,5,9.3),
    (9,2,5.5),(9,3,6.8),(9,4,5.8),(9,6,4.3),(9,5,4.5),
    (10,5,9.9),
    (13,3,8.0),(13,4,7.2),
    (14,2,8.5),(14,3,8.9),(14,4,8.9);

select * from reviews;

select title from series;

select title, rating from series
join reviews
on series.id = reviews.reviewer_id
order by rating desc
limit 3;

SELECT 
    title, ROUND(AVG(rating), 2) AS Ave_Rating
FROM
    series
        JOIN
    reviews ON series.id = reviews.reviewer_id
GROUP BY title
order by Ave_Rating asc;

SELECT first_name, last_name, rating from reviewers
join reviews
on reviewers.id = reviews.reviewer_id;
