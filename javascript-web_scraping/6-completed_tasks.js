#!/usr/bin/node

const request = require('request');

request.get({ url: process.argv[2] }, (err, resp, body) => {
  if (err) return;

  const dict = {};

  for (const todo of JSON.parse(body)) {
    if (!(todo.userId in dict) && todo.completed === true) {
      dict[todo.userId] = 0;
    }
    if (todo.completed === true) {
      dict[todo.userId] += 1;
    }
  }

  console.log(dict);
});
