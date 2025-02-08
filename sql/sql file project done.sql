USE editedlibrary;
-- 1
SELECT * from books;
--  # find the number of availalbe copies of the book total
select count(*) from books as b inner join loans as l on b.bookid=l.BookID where (b.title="dracula");
-- loaned books 
select count(*) from books as b inner join loans as l on b.bookid=l.BookID where (b.title="dracula") and l.returneddate is  null;
-- active
select count(*) from books as b inner join loans as l on b.bookid=l.BookID where (b.title="dracula") and l.returneddate is not null;
INSERT INTO  BOOKS(BOOKID,title,Author,Published,Barcode) Values(201,"Onyx Storm","Rebecca Yarros","2025",3100471143),(202,"The Let Them Theory","Mel Robbins","2025",3100471121),(203,"Open When","Julie Smith","2025",3100471191);
select * from books order by published desc
-- 4 
select * from books where barcode in (2855934983,4043822646)

--5 
select patronid from patrons where email ='jvaan@wisdompets.com'
-- 6
insert into loans (loanID,BookID,PatronID,loanDate,DueDate,Returneddate) Values (10003,11,50,"2020-08-25","2020-09-08",NULL),(10004,93,50,"2020-08-25","2020-09-08",NULL
--7 
select * from loans order by loandate desc
--8 
select * from patrons as p inner join loans as l on p.patronid = l.patronid where l.duedate ="2020-07-13"
-- 9
select * from books where barcode =6435968624
-- 10
select * from loans where bookid=105

-- 11
update loans  set returneddate ="2020-07-05" where loanid=1991
-- 12
select count(*) as countloan,p.firstname from patrons as p inner join loans as l on p.patronid=l.patronid group by p.firstname order by countloan limit 10
-- 13
select * from books as b left join loans as l on b.bookid =l.loanid where b.published between 1890 and 1990 and l.returneddate is not null



