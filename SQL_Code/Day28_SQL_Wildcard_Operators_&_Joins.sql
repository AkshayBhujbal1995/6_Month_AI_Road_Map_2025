mysql> -- Create a new database
mysql> CREATE DATABASE Day28SQLDemo;
Query OK, 1 row affected (0.78 sec)

mysql> 
mysql> -- Switch to the new database
mysql> USE Day28SQLDemo;
Database changed
mysql> -- PART 1: WILDCARD OPERATORS
mysql> -- Create Table CUSTOMERS
mysql> CREATE TABLE CUSTOMERS (
    ->     ID INT,
    ->     NAME VARCHAR(50),
    ->     AGE INT,
    ->     ADDRESS VARCHAR(100),
    ->     SALARY DECIMAL(10, 2)
    -> );
Query OK, 0 rows affected (2.50 sec)

mysql> 
mysql> INSERT INTO CUSTOMERS VALUES
    -> (1, 'Ramesh', 32, 'Ahmedabad', 2000.00),
    -> (2, 'Khilan', 25, 'Delhi', 1500.00),
    -> (3, 'Kaushik', 23, 'Kota', 2000.00),
    -> (4, 'Chaitali', 25, 'Mumbai', 6500.00),
    -> (5, 'Hardik', 27, 'Bhopal', 8500.00),
    -> (6, 'Komal', 22, 'MP', 4500.00),
    -> (7, 'Muffy', 24, 'Indore', 10000.00);
Query OK, 7 rows affected (0.38 sec)
Records: 7  Duplicates: 0  Warnings: 0

mysql> -- Wildcard Queries Using LIKE
mysql> -- 1. Salaries starting with 200
mysql> SELECT * FROM CUSTOMERS WHERE SALARY LIKE '200%';
+------+---------+------+-----------+---------+
| ID   | NAME    | AGE  | ADDRESS   | SALARY  |
+------+---------+------+-----------+---------+
|    1 | Ramesh  |   32 | Ahmedabad | 2000.00 |
|    3 | Kaushik |   23 | Kota      | 2000.00 |
+------+---------+------+-----------+---------+
2 rows in set (0.00 sec)

mysql> 
mysql> -- 2. Salaries containing 200 anywhere
mysql> SELECT * FROM CUSTOMERS WHERE SALARY LIKE '%200%';
+------+---------+------+-----------+---------+
| ID   | NAME    | AGE  | ADDRESS   | SALARY  |
+------+---------+------+-----------+---------+
|    1 | Ramesh  |   32 | Ahmedabad | 2000.00 |
|    3 | Kaushik |   23 | Kota      | 2000.00 |
+------+---------+------+-----------+---------+
2 rows in set (0.00 sec)

mysql> 
mysql> -- 3. Salaries with 00 in second and third positions
mysql> SELECT * FROM CUSTOMERS WHERE SALARY LIKE '_00%';
+------+---------+------+-----------+----------+
| ID   | NAME    | AGE  | ADDRESS   | SALARY   |
+------+---------+------+-----------+----------+
|    1 | Ramesh  |   32 | Ahmedabad |  2000.00 |
|    3 | Kaushik |   23 | Kota      |  2000.00 |
|    7 | Muffy   |   24 | Indore    | 10000.00 |
+------+---------+------+-----------+----------+
3 rows in set (0.00 sec)

mysql> 
mysql> -- 4. Start with 2 and at least 3 characters
mysql> SELECT * FROM CUSTOMERS WHERE SALARY LIKE '2_%_%';
+------+---------+------+-----------+---------+
| ID   | NAME    | AGE  | ADDRESS   | SALARY  |
+------+---------+------+-----------+---------+
|    1 | Ramesh  |   32 | Ahmedabad | 2000.00 |
|    3 | Kaushik |   23 | Kota      | 2000.00 |
+------+---------+------+-----------+---------+
2 rows in set (0.00 sec)

mysql> 
mysql> -- 5. End with 2
mysql> SELECT * FROM CUSTOMERS WHERE SALARY LIKE '%2';
Empty set (0.00 sec)

mysql> 
mysql> -- 6. Second character is 2 and ends with 3
mysql> SELECT * FROM CUSTOMERS WHERE SALARY LIKE '_2%3';
Empty set (0.00 sec)

mysql> 
mysql> -- 7. 5-digit salary starting with 2 and ending with 3
mysql> SELECT * FROM CUSTOMERS WHERE SALARY LIKE '2___3';
Empty set (0.00 sec)

mysql> -- SQL JOINS
mysql> -- Create Tables STUDENTS and COURSES
mysql> CREATE TABLE STUDENTS (
    ->     ID INT PRIMARY KEY,
    ->     NAME VARCHAR(50),
    ->     COURSE_ID INT
    -> );
Query OK, 0 rows affected (1.25 sec)

mysql> 
mysql> CREATE TABLE COURSES (
    ->     COURSE_ID INT PRIMARY KEY,
    ->     COURSE_NAME VARCHAR(50)
    -> );
Query OK, 0 rows affected (0.76 sec)

mysql> INSERT INTO STUDENTS VALUES
    -> (1, 'Akshay', 101),
    -> (2, 'Swara', 102),
    -> (3, 'Ravi', 103),
    -> (4, 'Neha', NULL);
Query OK, 4 rows affected (0.27 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> 
mysql> INSERT INTO COURSES VALUES
    -> (101, 'Math'),
    -> (102, 'Science'),
    -> (104, 'English');
Query OK, 3 rows affected (0.34 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> --INNER JOIN
    -> -- Show only matching records from both tables
    -> SELECT s.ID, s.NAME, c.COURSE_NAME
    -> FROM STUDENTS s
    -> INNER JOIN COURSES c ON s.COURSE_ID = c.COURSE_ID;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '--INNER JOIN

SELECT s.ID, s.NAME, c.COURSE_NAME
FROM STUDENTS s
INNER JOIN COUR' at line 1
mysql> -- INNER JOIN: Show only matching records from both tables
mysql> SELECT s.ID, s.NAME, c.COURSE_NAME
    -> FROM STUDENTS s
    -> INNER JOIN COURSES c ON s.COURSE_ID = c.COURSE_ID;
+----+--------+-------------+
| ID | NAME   | COURSE_NAME |
+----+--------+-------------+
|  1 | Akshay | Math        |
|  2 | Swara  | Science     |
+----+--------+-------------+
2 rows in set (0.06 sec)

mysql> -- LEFT JOIN
mysql> -- Show all students, even if course is missing
mysql> SELECT s.ID, s.NAME, c.COURSE_NAME
    -> FROM STUDENTS s
    -> LEFT JOIN COURSES c ON s.COURSE_ID = c.COURSE_ID;
+----+--------+-------------+
| ID | NAME   | COURSE_NAME |
+----+--------+-------------+
|  1 | Akshay | Math        |
|  2 | Swara  | Science     |
|  3 | Ravi   | NULL        |
|  4 | Neha   | NULL        |
+----+--------+-------------+
4 rows in set (0.17 sec)

mysql> -- RIGHT JOIN 
mysql> -- Show all courses, even if no student enrolled
mysql> SELECT s.ID, s.NAME, c.COURSE_NAME
    -> FROM STUDENTS s
    -> RIGHT JOIN COURSES c ON s.COURSE_ID = c.COURSE_ID;
+------+--------+-------------+
| ID   | NAME   | COURSE_NAME |
+------+--------+-------------+
|    1 | Akshay | Math        |
|    2 | Swara  | Science     |
| NULL | NULL   | English     |
+------+--------+-------------+
3 rows in set (0.00 sec)

mysql> -- FULL OUTER JOIN (via UNION in MySQL)
mysql> -- Combine LEFT and RIGHT JOIN for full outer effect
mysql> SELECT s.ID, s.NAME, c.COURSE_NAME
    -> FROM STUDENTS s
    -> LEFT JOIN COURSES c ON s.COURSE_ID = c.COURSE_ID
    -> UNION
    -> SELECT s.ID, s.NAME, c.COURSE_NAME
    -> FROM STUDENTS s
    -> RIGHT JOIN COURSES c ON s.COURSE_ID = c.COURSE_ID;
+------+--------+-------------+
| ID   | NAME   | COURSE_NAME |
+------+--------+-------------+
|    1 | Akshay | Math        |
|    2 | Swara  | Science     |
|    3 | Ravi   | NULL        |
|    4 | Neha   | NULL        |
| NULL | NULL   | English     |
+------+--------+-------------+
5 rows in set (0.07 sec)

mysql> notee;
