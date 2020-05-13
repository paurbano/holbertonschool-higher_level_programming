#!/usr/bin/node
// Use  Star wars API to get

const request = require('request');
const fs = require('fs');
function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
      if (err) {
        return console.log(err);
      }
    });
  }
}
request(process.argv[2], callback);
