#!/usr/bin/python3
"""
Module States
script that lists all states with a name starting with N (upper N)
"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    MY_USER = argv[1]
    MY_PASSWD = argv[2]
    MY_DB = argv[3]
    param = str(argv[4])

    '''Open Database connection'''
    mydb = MySQLdb.connect(host="localhost",
                           user=MY_USER,
                           passwd=MY_PASSWD,
                           db=MY_DB)

    '''Create cursor for operate over DB'''
    myCursor = mydb.cursor()
    query = "select * from states where name = '{}'".format(param)

    '''pass and execute a SQL sentence'''
    myCursor.execute(query)

    '''retrive records and fill cursor'''
    states = myCursor.fetchall()

    '''Print rows'''
    for state in states:
        print(state)

    '''close cursor'''
    myCursor.close()

    '''close connection to DB'''
    mydb.close()
