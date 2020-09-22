#!/usr/bin/node
const request = require('request');
const newDict = {};
request(process.argv[2], function (error, response, body) {
  if (error) console.log('error:', error);
  const result = JSON.parse(body);
  result.forEach((currentItem) => {
    if (!newDict[currentItem.userId]) {
      newDict[currentItem.userId] = 0;
    }
    if (currentItem.completed === true) {
      newDict[currentItem.userId]++;
    }
  });
  console.log(newDict);
});
