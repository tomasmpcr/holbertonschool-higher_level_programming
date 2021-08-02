#!/usr/bin/node
const { argv } = require('process');

console.log(fact(parseInt(argv[2])));

function fact (numMax, i = 1) {
  if (isNaN(numMax) || numMax <= i) {
    return (i);
  }
  return (fact(numMax, i + 1) * i);
}
