#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
const searched = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach((film) => {
      if (film.characters.includes(searched)) count++;
    });
    console.log(count);
  }
});
