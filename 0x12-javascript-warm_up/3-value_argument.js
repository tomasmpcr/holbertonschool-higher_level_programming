#!/usr/bin/node
const { argv } = require('process');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  for (let i = 2; argv[i] != undefined; i++) {
    console.log(argv[i]);
  }
}
