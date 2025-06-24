tee c/Sql_output_files/sql_output_Opeators_log.txt;
Logging to file 'c/Sql_output_files/sql_output_Opeators_log.txt'

mysql> CREATE DATABASE OperatorDemo;
Query OK, 1 row affected (0.25 sec)

mysql> USE OperatorDemo;
Database changed
mysql> CREATE TABLE Students (
    ->   ID INT PRIMARY KEY AUTO_INCREMENT,
    ->   Name VARCHAR(50),
    ->   Marks INT,
    ->   Age INT
    -> );
Query OK, 0 rows affected (3.20 sec)

mysql> INSERT INTO Students (Name, Marks, Age) VALUES 
    -> ('Akshay', 85, 20),
    -> ('Swara', 92, 19),
    -> ('Ravi', 76, 21),
    -> ('Neha', 89, 22),
    -> ('Amit', 66, 20);
Query OK, 5 rows affected (0.59 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> -- Arithmetic Operators +, -, *, /, %
mysql> 50 + 50;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '50 + 50' at line 1
mysql> select 50 + 50;
+---------+
| 50 + 50 |
+---------+
|     100 |
+---------+
1 row in set (0.00 sec)

mysql> select 100 - 80;
+----------+
| 100 - 80 |
+----------+
|       20 |
+----------+
1 row in set (0.00 sec)

mysql> select 1000 * 3;
+----------+
| 1000 * 3 |
+----------+
|     3000 |
+----------+
1 row in set (0.00 sec)

mysql> select 40 / 2;
+---------+
| 40 / 2  |
+---------+
| 20.0000 |
+---------+
1 row in set (0.00 sec)

mysql> select 40 % 2;
+--------+
| 40 % 2 |
+--------+
|      0 |
+--------+
1 row in set (0.00 sec)

mysql> -- Add 5 marks to each student
mysql> SELECT Name, Marks, Marks + 5 AS UpdatedMarks FROM Students;
+--------+-------+--------------+
| Name   | Marks | UpdatedMarks |
+--------+-------+--------------+
| Akshay |    85 |           90 |
| Swara  |    92 |           97 |
| Ravi   |    76 |           81 |
| Neha   |    89 |           94 |
| Amit   |    66 |           71 |
+--------+-------+--------------+
5 rows in set (0.00 sec)

mysql> -- Subtract 2 years from each student's age
mysql> SELECT Name, Age, Age - 2 AS Age2YearsAgo FROM Students;
+--------+------+--------------+
| Name   | Age  | Age2YearsAgo |
+--------+------+--------------+
| Akshay |   20 |           18 |
| Swara  |   19 |           17 |
| Ravi   |   21 |           19 |
| Neha   |   22 |           20 |
| Amit   |   20 |           18 |
+--------+------+--------------+
5 rows in set (0.00 sec)

mysql> -- Multiply marks by 2
mysql> SELECT Name, Marks, Marks * 2 AS DoubleMarks FROM Students;
+--------+-------+-------------+
| Name   | Marks | DoubleMarks |
+--------+-------+-------------+
| Akshay |    85 |         170 |
| Swara  |    92 |         184 |
| Ravi   |    76 |         152 |
| Neha   |    89 |         178 |
| Amit   |    66 |         132 |
+--------+-------+-------------+
5 rows in set (0.00 sec)

mysql> -- Divide marks by 2
mysql> SELECT Name, Marks, Marks / 2 AS HalfMarks FROM Students;
+--------+-------+-----------+
| Name   | Marks | HalfMarks |
+--------+-------+-----------+
| Akshay |    85 |   42.5000 |
| Swara  |    92 |   46.0000 |
| Ravi   |    76 |   38.0000 |
| Neha   |    89 |   44.5000 |
| Amit   |    66 |   33.0000 |
+--------+-------+-----------+
5 rows in set (0.00 sec)

mysql> -- Modulus: Remainder of marks divided by 10
mysql> SELECT Name, Marks, Marks % 10 AS MarksMod10 FROM Students;
+--------+-------+------------+
| Name   | Marks | MarksMod10 |
+--------+-------+------------+
| Akshay |    85 |          5 |
| Swara  |    92 |          2 |
| Ravi   |    76 |          6 |
| Neha   |    89 |          9 |
| Amit   |    66 |          6 |
+--------+-------+------------+
5 rows in set (0.00 sec)

mysql> -- Comparison Operators  =, <>, >, <, >=, <=
mysql> -- 1 is True , 0 is False
mysql> select 3 = 3;
+-------+
| 3 = 3 |
+-------+
|     1 |
+-------+
1 row in set (0.00 sec)

mysql> select 3 = 4;
+-------+
| 3 = 4 |
+-------+
|     0 |
+-------+
1 row in set (0.00 sec)

mysql> select 85 > -8888;
+------------+
| 85 > -8888 |
+------------+
|          1 |
+------------+
1 row in set (0.09 sec)

mysql> select 85 < -8888;
+------------+
| 85 < -8888 |
+------------+
|          0 |
+------------+
1 row in set (0.00 sec)

mysql> -- Students who scored exactly 85
mysql> SELECT * FROM Students WHERE Marks = 85;
+----+--------+-------+------+
| ID | Name   | Marks | Age  |
+----+--------+-------+------+
|  1 | Akshay |    85 |   20 |
+----+--------+-------+------+
1 row in set (0.00 sec)

mysql> -- Students who scored not equal to 85
mysql> SELECT * FROM Students WHERE Marks <> 85;
+----+-------+-------+------+
| ID | Name  | Marks | Age  |
+----+-------+-------+------+
|  2 | Swara |    92 |   19 |
|  3 | Ravi  |    76 |   21 |
|  4 | Neha  |    89 |   22 |
|  5 | Amit  |    66 |   20 |
+----+-------+-------+------+
4 rows in set (0.00 sec)

mysql> -- Students with marks greater than 80
mysql> SELECT * FROM Students WHERE Marks > 80;
+----+--------+-------+------+
| ID | Name   | Marks | Age  |
+----+--------+-------+------+
|  1 | Akshay |    85 |   20 |
|  2 | Swara  |    92 |   19 |
|  4 | Neha   |    89 |   22 |
+----+--------+-------+------+
3 rows in set (0.00 sec)

mysql> -- Students younger than 21
mysql> SELECT * FROM Students WHERE Age < 21;
+----+--------+-------+------+
| ID | Name   | Marks | Age  |
+----+--------+-------+------+
|  1 | Akshay |    85 |   20 |
|  2 | Swara  |    92 |   19 |
|  5 | Amit   |    66 |   20 |
+----+--------+-------+------+
3 rows in set (0.00 sec)

mysql> -- Marks greater than or equal to 89
mysql> SELECT * FROM Students WHERE Marks >= 89;
+----+-------+-------+------+
| ID | Name  | Marks | Age  |
+----+-------+-------+------+
|  2 | Swara |    92 |   19 |
|  4 | Neha  |    89 |   22 |
+----+-------+-------+------+
2 rows in set (0.00 sec)

mysql> -- Age less than or equal to 20
mysql> SELECT * FROM Students WHERE Age <= 20;
+----+--------+-------+------+
| ID | Name   | Marks | Age  |
+----+--------+-------+------+
|  1 | Akshay |    85 |   20 |
|  2 | Swara  |    92 |   19 |
|  5 | Amit   |    66 |   20 |
+----+--------+-------+------+
3 rows in set (0.00 sec)

mysql> -- Logical Operators AND, OR , NOT
mysql> -- Students with marks > 80 AND age < 21
mysql> SELECT * FROM Students WHERE Marks > 80 AND Age < 21;
+----+--------+-------+------+
| ID | Name   | Marks | Age  |
+----+--------+-------+------+
|  1 | Akshay |    85 |   20 |
|  2 | Swara  |    92 |   19 |
+----+--------+-------+------+
2 rows in set (0.00 sec)

mysql> -- Students with marks > 90 OR age < 20
mysql> SELECT * FROM Students WHERE Marks > 90 OR Age < 20;
+----+-------+-------+------+
| ID | Name  | Marks | Age  |
+----+-------+-------+------+
|  2 | Swara |    92 |   19 |
+----+-------+-------+------+
1 row in set (0.00 sec)

mysql> -- Students who are NOT aged 20
mysql> SELECT * FROM Students WHERE NOT Age = 20;
+----+-------+-------+------+
| ID | Name  | Marks | Age  |
+----+-------+-------+------+
|  2 | Swara |    92 |   19 |
|  3 | Ravi  |    76 |   21 |
|  4 | Neha  |    89 |   22 |
+----+-------+-------+------+
3 rows in set (0.00 sec)

mysql> notee;
