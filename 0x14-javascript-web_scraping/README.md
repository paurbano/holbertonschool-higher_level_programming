# 0x14. Javascript - Web scraping

## General
* Why Javascript programming is amazing
* How to manipulate JSON data
* How to use request and fetch API
* How to read and write a file using fs module

# Install Node 10
    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs

# Install semi-standard
Documentation

    $ sudo npm install semistandard --global

# Install request module and use it
Documentation

    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules

## 0. Readme
Write a script that reads and prints the content of a file.

* The first argument is the file path
* The content of the file must be read in utf-8
* If an error occurred during the reading, print the error object

Example

    guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
    C is super fun!
    guillaume@ubuntu:~/0x14$ cat cisfun
    C is super fun!
    guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
    { Error: ENOENT: no such file or directory, open 'doesntexist'
        at Error (native)
    errno: -2,
    code: 'ENOENT',
    syscall: 'open',
    path: 'doesntexist' }
    guillaume@ubuntu:~/0x14$ 

File: `0-readme.js`

## 1. Write me
Write a script that writes a string to a file.

* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in utf-8
* If an error occurred during while writing, print the error object

Example

    guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
    guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
    Python is cool
    guillaume@ubuntu:~/0x14$ 

Repo:
File: `1-writeme.js`

## 2. Status code
Write a script that display the status code of a GET request.

* The first argument is the URL to request (GET)
* The status code must be printed like this: code: <status code>
* You must use the module request

Example

    guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/status
    code: 200
    guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
    code: 404
    guillaume@ubuntu:~/0x14$

## 5. Loripsum
Write a script that gets the contents of a webpage and stores it in a file.

* The first argument is the URL to request
* The second argument the file path to store the body response
* The file must be UTF-8 encoded
* You must use the module `request`

File: `5-request_store.js`

## 6. How many completed?
Write a script that computes the number of tasks completed by user id.

* The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
* You must use the module `request`

example

    guillaume@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
    { '1': 11,
    '2': 8,
    '3': 7,
    '4': 6,
    '5': 12,
    '6': 6,
    '7': 9,
    '8': 11,
    '9': 8,
    '10': 12 }
    guillaume@ubuntu:~/0x14$

File: `6-completed_tasks.js`