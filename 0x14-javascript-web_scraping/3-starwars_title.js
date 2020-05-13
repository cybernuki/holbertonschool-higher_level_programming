#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const title = JSON.parse(body).title;
    console.log(`${title}`);
  }
});
