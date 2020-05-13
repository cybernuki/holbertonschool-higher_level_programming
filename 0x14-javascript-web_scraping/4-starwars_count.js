#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;

request(url, function (error, response, body) {
  if (!error) {
    const films = JSON.parse(body).results;
    const count = films.reduce((count, film) => {
      const filter = film.characters.find((character) => character.endsWith('/18/'));
      return (filter) ? count + 1 : count;
    }, 0);
    console.log(count);
  }
});
