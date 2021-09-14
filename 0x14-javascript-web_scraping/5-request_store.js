#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    try {
      fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
        if (err) {
          return console.log(err);
        }
      });
    } catch (err) {
      console.error(err);
    }
  }
});
