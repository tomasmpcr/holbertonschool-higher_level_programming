#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!parseInt(w) || w <= 0) {
      return;
    }

    if (!parseInt(h) || h <= 0) {
      return;
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
