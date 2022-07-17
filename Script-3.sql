select oid, * from income_expense ie 

select oid, * from bank_statement bs 

delete * from bank_statement 






select oid, * from receipt r 

select * from "member" m 

SELECT * FROM "member" m WHERE id like "%%1%%"

select * from receipt r where date like "%%12/11%%"

select * from receipt afr union all select * from receipt r where member_name like "%%DQ%%"

SELECT * from receipt afr where member_name like "%%ANIK%%" UNION ALL select * from receipt r where member_name like "%%ANIK%%"



update "member" set date = "12/12/2004" where id = 1

update receipt set amount = "0" where oid = 3

select oid, * from receipt r WHERE oid = 3

select oid, * from receipt r  where oid = 2 or 3

select * from receipt r where payment_type like '%%Admit%%' or payment_type like "%%Fine%%"

select oid, * from receipt r where payment_type LIKE '%%Due%%' OR payment_type LIKE '%%Current%%' OR payment_type LIKE '%%Advance%%'

select * from receipt r where date like "%%18/01/2025" and oid like "%1%" or oid like "%2%"

select paid_for from receipt r 

select * from receipt r 

select oid, * from bank_statement bs 

select oid, * FROM bank_statement bs WHERE account_type like "%FDR%"






drop table "member" 

drop table receipt

drop table bank_statement 