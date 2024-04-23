#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i += 1) {
      let row = '';
      for (let j = 0; j < this.width; j += 1) row += 'X';
      console.log(row);
    }
  }
}

module.exports = Rectangle;
