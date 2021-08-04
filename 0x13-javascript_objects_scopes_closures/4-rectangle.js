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

  rotate () {
    const x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
