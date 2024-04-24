#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < size; i++) {
      const row = '';
      for (let j = 0; j < size; j++) {
        if (c === undefined) row += 'X';
        row += 'C';
      }
      console.log(row);
    }
  }
}

module.exports = Square;
