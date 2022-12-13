#!/usr/bin/node

const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, function (err, resp, body) {
  if (err) return;

  const movies = JSON.parse(body).results;

  let count = 0;
  for (const movie of movies) {
    const charList = movie.characters;
    console.log(movie.title);
    if (charList.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
