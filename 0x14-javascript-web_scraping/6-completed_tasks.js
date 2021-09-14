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
    const obj = JSON.parse(body);
    const objReturn = {};
    obj.forEach(element => {
      if (element.completed) {
        if (objReturn[element.userId] !== undefined) {
          objReturn[element.userId]++;
        } else {
          objReturn[element.userId] = 1;
        }
      }
    });
    console.log(objReturn);
  }
});
