#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i += 1) {
      let row = '';
      for (let j = 0; j < this.width; j += 1) row += 'X';
      console.log(row);
    }
  }

  rotate() {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double() {
    return (this.height * 2, this.width * 2);
  }
}

module.exports = Rectangle;
