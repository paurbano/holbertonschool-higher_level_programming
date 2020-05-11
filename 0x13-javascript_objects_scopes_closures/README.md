# 0x13. Javascript - Objects, Scopes and Closures

# General
* Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
* How to create an object in Javascript
* What this means
* What undefined means
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another

## 0. Rectangle #0
Write an empty class Rectangle that defines a rectangle:

You must use the class notation for defining your class

    guillaume@ubuntu:~/0x13$ cat 0-main.js
    #!/usr/bin/node
    const Rectangle = require('./0-rectangle');

    const r1 = new Rectangle();
    console.log(r1);
    console.log(r1.constructor);

    guillaume@ubuntu:~/0x13$ ./0-main.js
    Rectangle {}
    [Function: Rectangle]
    guillaume@ubuntu:~/0x13$

File: `0-rectangle.js`