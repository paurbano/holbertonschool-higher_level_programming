#!/usr/bin/node
// Use  Star wars API to get

const request = require('request');

function callback (error, response, body) {
  let count = 0;
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body).results;

    for (const result of info) {
      for (const character of result.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
  }
  console.log(count);
}
request(process.argv[2], callback);
