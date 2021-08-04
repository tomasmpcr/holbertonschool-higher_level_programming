#!/usr/bin/node
const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c = 'X') {
    let cuadrado = '';
    for (let i = 0; i < this.width; i++) {
      cuadrado += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(cuadrado);
    }
  }
}

module.exports = Square;
