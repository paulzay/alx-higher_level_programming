#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor(size) {
    super(w, h);
    this.w = size;
  }
}

module.exports = Square;
