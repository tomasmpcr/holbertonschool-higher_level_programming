#!/usr/bin/node
const request = require('request');

const options = {
    url: process.argv[2],
    method: 'GET'
};

request(options, function(err, res, body) {
    console.log('code: '+res.statusCode);
});
