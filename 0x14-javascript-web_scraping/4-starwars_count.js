#!/usr/bin/node
// Use  Star wars API to get

const request = require('request');
const options = {
  url: 'https://swapi-api.hbtn.io/api/people/18',
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    console.log(info.films.length);
  }
}
request(options, callback);
