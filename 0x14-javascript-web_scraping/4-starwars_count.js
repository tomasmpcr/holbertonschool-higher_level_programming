#!/usr/bin/node
const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const obj = JSON.parse(body);
    obj.results.forEach(element => {
      element.characters.forEach(element2 => {
        if (element2.includes('/18/')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
