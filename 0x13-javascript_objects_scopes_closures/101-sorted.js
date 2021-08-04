#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const property in dict) {
  if (newDict[dict[property]] === undefined) {
    newDict[dict[property]] = [property];
  } else {
    newDict[dict[property]].push(property);
  }
}
console.log(newDict);
