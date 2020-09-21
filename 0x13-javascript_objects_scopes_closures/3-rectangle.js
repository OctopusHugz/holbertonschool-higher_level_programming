#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const arr = [];
    for (let i = 0; i < this.width; i++) {
      arr.push('X');
    }
    for (let j = 0; j < this.height; j++) {
      console.log(arr.join(''));
    }
  }
}
module.exports = Rectangle;
