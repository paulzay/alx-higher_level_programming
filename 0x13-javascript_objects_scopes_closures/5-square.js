#!/usr/bin/node

const Rectangle = require('./4-rectangle');

Rectangle;
class Square extends Rectangle {
  constructor(size) {
    super(w, h);
    this.size = size;
  }
}

module.exports = Square;
