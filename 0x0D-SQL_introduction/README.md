# 0x0D. SQL - Introduction

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

# 0. List databases
script that lists all databases of your MySQL server.

    guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    Database
    information_schema
    mysql
    performance_schema
    guillaume@ubuntu:~/$ 

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: 0x0D-SQL_introduction
* File: 0-list_databases.sql

# 1. Create a database
Write a script that creates the database hbtn_0c_0 in your MySQL server.

* If the database hbtn_0c_0 already exists, your script should not fail
* You are not allowed to use the SELECT or SHOW statements


    guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    Database
    information_schema
    hbtn_0c_0
    mysql
    performance_schema
    guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    guillaume@ubuntu:~/$

# 2. Delete a database
Write a script that deletes the database hbtn_0c_0 in your MySQL server.

* If the database hbtn_0c_0 doesn’t exist, your script should not fail
* You are not allowed to use the SELECT or SHOW statements

    guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
    Enter password: 

# 3. List tables
Write a script that lists all the tables of a database in your MySQL server.

* The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

    guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
    Enter password: 
    Tables_in_mysql
    columns_priv
    db
    event
    func
    general_log
    help_category
    help_keyword
    help_relation
    help_topic
    host
    ndb_binlog_index
    plugin
    proc
    procs_priv
    proxies_priv
    servers
    slow_log
    tables_priv
    time_zone
    time_zone_leap_second
    time_zone_name
    time_zone_transition
    time_zone_transition_type
    user
    guillaume@ubuntu:~/$

# 4. First table
Write a script that creates a table called first_table in the current database in your MySQL server.

* first_table description:
    * id INT
    * name VARCHAR(256)
* The database name will be passed as an argument of the mysql command
* If the table first_table already exists, your script should not fail
* You are not allowed to use the SELECT or SHOW statements

    guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 

# 5. Full description
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

* The database name will be passed as an argument of the mysql command
* You are not allowed to use the DESCRIBE or EXPLAIN statements

    guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    Table   Create Table
    first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
    guillaume@ubuntu:~/$

# 6. List all in table
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

    guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    guillaume@ubuntu:~/$

* All fields should be printed
* The database name will be passed as an argument of the mysql command

# 7. First add
Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

    guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password:
    guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    id  name
    89  Holberton School
    89  Holberton School
    89  Holberton School
    guillaume@ubuntu:~/$ 

* New row:
    * id = 89
    * name = Holberton School
* The database name will be passed as an argument of the mysql command

# 8. Count 89
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

    guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
    Enter password: 
    3
    guillaume@ubuntu:~/$ 

* The database name will be passed as an argument of the mysql command

# 9. Full creation
Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

    guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    guillaume@ubuntu:~/$ 

* second_table description:
    * id INT
    * name VARCHAR(256)
    * score INT
* The database name will be passed as an argument to the mysql command
* If the table second_table already exists, your script should not fail
* You are not allowed to use the SELECT and SHOW statements
* Your script should create these records:
    * id = 1, name = “John”, score = 10
    * id = 2, name = “Alex”, score = 3
    * id = 3, name = “Bob”, score = 14
    * id = 4, name = “George”, score = 8

# 10. List by best
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

    guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
    Enter password: 
    score   name
    14  Bob
    10  John
    8   George
    3   Alex
    guillaume@ubuntu:~/$ 
    
* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the mysql command

# 11. Select the best
Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the mysql command

# 12. Cheating is bad
Write a script that updates the score of Bob to 10 in the table second_table.

* You are not allowed to use Bob’s id value, only the name field
* The database name will be passed as an argument of the mysql command

# 13. Score too low
Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

* The database name will be passed as an argument of the mysql command

# 14. Average
Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

* The result column name should be average
* The database name will be passed as an argument of the mysql command

# 15. Number by score
Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

* The result should display:
* the score
* the number of records for this score with the label number
* The list should be sorted by the number of records (descending)
* The database name will be passed as an argument to the mysql command

# 16. Say my name
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

# 17. Go to UTF8
Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

# 18. Temperatures #0
Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

# 19. Temperatures #1
Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

# 20. Temperatures #2
Write a script that displays the max temperature of each state (ordered by State name).

# AUTHOR
## Pablo Andres Urbano - <1283@holbertonschool.com>