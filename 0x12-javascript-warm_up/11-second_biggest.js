#!/usr/bin/node
const { argv } = require('process');

argv.splice(0, 2);

if (argv.length <= 1) {
  console.log(1);
} else {
  const newArray = argv.sort(function (a, b) {
    return (a - b);
  });

  console.log(newArray[newArray.length - 2]);
}
