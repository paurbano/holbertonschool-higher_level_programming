# 0x11. Python - Network #1
## General
* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

## 0. What's my status?
Write a Python script that fetches https://intranet.hbtn.io/status

* You must use the package urllib
* You are not allowed to import any packages other than urllib
* The body of the response must be displayed like the following example (tabulation before -)
* You must use a with statement


    guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
    Body response:$
        - type: <class 'bytes'>$
        - content: b'OK'$
        - utf8 content: OK$
    guillaume@ubuntu:~/0x11$

## 1. Response header value #0
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

* You must use the packages urllib and sys
* You are not allow to import packages other than urllib and sys
* The value of this variable is different for each request
* You don’t need to check arguments passed to the script (number or type)
* You must use a with statement


    guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://intranet.hbtn.io
    ade2627e-41dd-4c34-b9d9-a0fa0f47b237
    guillaume@ubuntu:~/0x11$ 
    guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://intranet.hbtn.io
    6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
    guillaume@ubuntu:~/0x11$

## 2. POST an email #0
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

* The email must be sent in the email variable
* You must use the packages urllib and sys
* You are not allowed to import packages other than urllib and sys
* You don’t need to check arguments passed to the script (number or type)
* You must use the with statement


    guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
    Your email is: hr@holbertonschool.com
    guillaume@ubuntu:~/0x11$

# Author
Pablo Andres Urbano - (1283@holbertonschool.com)
