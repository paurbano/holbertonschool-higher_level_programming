#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    sum = 0
    for n in range(len(argv)):
        if n != 0:
            sum = sum + int(argv[n])

    print("{}".format(sum))
