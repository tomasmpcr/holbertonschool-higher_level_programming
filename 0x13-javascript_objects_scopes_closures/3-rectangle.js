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

  print () {
    let cuadrado = '';
    for (let i = 0; i < this.width; i++) {
      cuadrado += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(cuadrado);
    }
  }
}

module.exports = Rectangle;
