#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  const newDict = {};
  if (error) console.log('error:', error);
  const tasks = JSON.parse(body);
  tasks.forEach((task) => {
    if (!newDict[task.userId] && task.completed) {
      newDict[task.userId] = 0;
    }
    if (task.completed) {
      newDict[task.userId]++;
    }
  });
  console.log(newDict);
});
