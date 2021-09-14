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
    console.log('code: ' + res.statusCode);
  }
});
