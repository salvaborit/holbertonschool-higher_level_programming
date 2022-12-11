#!/usr/bin/node

module.exports =
  class Rectangle {
    constructor (w, h) {
      if (parseInt(w) > 0 && parseInt(h) > 0) {
        this.width = w;
        this.height = h;
      }
    }

    print () {
      for (let row = 0; row < this.height; row++) {
        for (let col = 0; col < this.width; col++) {
          process.stdout.write('X');
        }
        console.log('');
      }
    }
  };
