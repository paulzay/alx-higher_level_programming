#!/usr/bin/node

const Sq = require('./5-square')

class Square extends Sq {
  charPrint(c) {
    for (let i = 0; i < this.height; i++) {
      const row = '';
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) row += 'X';
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
