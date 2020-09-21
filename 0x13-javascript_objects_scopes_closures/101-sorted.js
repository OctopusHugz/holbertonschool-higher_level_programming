#!/usr/bin/node
const outerDict = require('./101-data');
const innerDict = outerDict.dict;
const newDict = {};
for (var key in innerDict) {
  var value = innerDict[key];
  if (newDict[value]) newDict[value].push(key);
  else {
    newDict[value] = [];
    newDict[value].push(key);
  }
}
console.log(newDict);
