#!/usr/bin/node

const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log('Code:', response.statusCode); // Print the response status code if a response was received
});
