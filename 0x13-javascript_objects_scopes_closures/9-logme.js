#!/usr/bin/node
global.count = 0;
exports.logMe = function (item) {
  console.log(global.count + ': ' + item);
  global.count++;
};
