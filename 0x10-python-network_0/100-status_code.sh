#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sI "$1" | grep -Fi 'HTTP' | cut -d ' ' -f2- | cut -d ' ' -f1
