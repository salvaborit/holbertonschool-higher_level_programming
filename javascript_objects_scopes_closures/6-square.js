#!/usr/bin/node
const Sq = require('./5-square');

module.exports =
  class Square extends Sq {
    charPrint (c = 'X') {
      for (let row = 0; row < this.height; row++) {
        for (let col = 0; col < this.width; col++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
  };
