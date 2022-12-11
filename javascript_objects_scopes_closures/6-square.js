#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports =
  class Square extends Rectangle {
    constructor (size) {
      super(size, size);
    }

    charPrint (c = 'X') {
      for (let row = 0; row < this.height; row++) {
        for (let col = 0; col < this.width; col++) {
          process.stdout.write(c);
        }
        console.log('');
      }
    }
};
