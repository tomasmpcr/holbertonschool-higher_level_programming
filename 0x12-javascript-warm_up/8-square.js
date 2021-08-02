#!/usr/bin/node
const { argv } = require('process');

if (parseInt(argv[2])) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    let cadena = '';
    for (let j = 0; j < parseInt(argv[2]); j++) {
      cadena += 'X';
    }
    console.log(cadena);
  }
} else {
  console.log('Missing size');
}
