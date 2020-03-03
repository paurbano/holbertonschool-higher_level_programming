# 0x0E. SQL - More queries

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

# 0. My privileges!
Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

    guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_1' on host 'localhost'
    guillaume@ubuntu:~/$ 
    guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
    Enter password: 
    guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
    Enter password: 
    guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    Grants for user_0d_1@localhost
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
    ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
    guillaume@ubuntu:~/$ 

Repo:

* GitHub repository: holbertonschool-higher_level_programming
* Directory: 0x0E-SQL_more_queries
* File: 0-privileges.sql

# 1. Root user
Write a script that creates the MySQL server user user_0d_1.

    guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
    Enter password: 
    Grants for user_0d_1@localhost
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
    ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
    guillaume@ubuntu:~/$ 

* user_0d_1 should have all privileges on your MySQL server
* The user_0d_1 password should be set to user_0d_1_pwd
* If the user user_0d_1 already exists, your script should not fail
