#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (var key in dict) {
  var value = dict[key];
  if (newDict[value]) newDict[value].push(key);
  else {
    newDict[value] = [];
    newDict[value].push(key);
  }
}
console.log(newDict);
