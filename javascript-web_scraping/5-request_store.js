#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request.get({ url: process.argv[2] }, (err, resp, body) => {
  if (err) return;
  fs.writeFile(process.argv[3], body, (err) => {
    if (err) console.error(err);
  });
});
