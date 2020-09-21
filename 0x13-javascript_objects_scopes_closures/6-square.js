#!/usr/bin/node
const firstSquare = require('./5-square');
class Square extends firstSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const arr = [];
    for (let i = 0; i < this.width; i++) {
      if (typeof c === 'undefined') arr.push('X');
      else arr.push(c);
    }
    for (let j = 0; j < this.height; j++) {
      console.log(arr.join(''));
    }
  }
}
module.exports = Square;
