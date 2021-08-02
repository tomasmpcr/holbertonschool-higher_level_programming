#!/usr/bin/node
const { argv } = require('process');

if (parseInt(argv[2])) {
  console.log(fact(parseInt(argv[2])));
} else {
 console.log(1); 
}

function fact (numMax, i = 1) {
  if (numMax <= i) {
    return (i);
  }
  return (fact(numMax, i + 1) * i);
}
