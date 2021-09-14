#!/usr/bin/node
const request = require('request');
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  method: 'GET'
};

request(options, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(body);
    for (let i = 0; i < obj.characters.length; i++) {
      const options2 = {
        url: obj.characters[i],
        method: 'GET'
      };

      request(options2, function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          const obj2 = JSON.parse(body);
          console.log(obj2.name);
        }
      });
    }
  }
});
