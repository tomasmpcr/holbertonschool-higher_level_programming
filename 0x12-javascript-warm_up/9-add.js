#!/usr/bin/node
const { argv } = require('process');

add(argv[2], argv[3]);

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
