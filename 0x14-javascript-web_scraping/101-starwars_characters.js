#!/usr/bin/node
const request = require('request');

preuba();

async function preuba () {
  const p1 = (await requestFunc('https://swapi-api.hbtn.io/api/films/' + process.argv[2])).characters;
  for (let i = 0; i < p1.length; i++) {
    console.log((await requestFunc(p1[i])).name);
  }
}

function requestFunc (url) {
  return (new Promise((resolve, reject) => {
    const options = {
      url: url,
      method: 'GET'
    };

    request(options, function (err, res, body) {
      if (err) {
        reject(err);
      } else {
        const obj = JSON.parse(body);
        resolve(obj);
      }
    });
  }));
}
