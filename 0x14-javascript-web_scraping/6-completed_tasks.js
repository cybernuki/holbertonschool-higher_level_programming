#!/usr/bin/node
const request = require('request');

const url = `${process.argv[2]}`;

request(url, (error, Response, body) => {
  if (!error) {
    const result = {};
    JSON.parse(body).forEach((task) => {
      const user = task.userId;
      const done = task.completed;
      if (!result[user]) result[user] = 0;
      result[user] = (done) ? result[user] + 1 : result[user];
    });
    console.log(result);
  }
});
