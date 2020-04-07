#!/bin/bash
# sends a POST request to the URL, and set 2 variables and displays the body of the response
curl -sL "$1" -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
