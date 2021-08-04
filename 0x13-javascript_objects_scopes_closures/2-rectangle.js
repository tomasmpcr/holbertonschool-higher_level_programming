#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (!parseInt(width) || width <= 0) {
      console.log(width);
      return;
    }

    if (!parseInt(height) || height <= 0) {
      return;
    }

    this.width = width;
    this.height = height;
  }
}

module.exports = Rectangle;
