#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) row += c || 'X';
      console.log(row);
    }
  }
}

module.exports = Square;
