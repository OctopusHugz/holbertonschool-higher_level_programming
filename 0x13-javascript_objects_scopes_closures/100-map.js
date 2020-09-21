#!/usr/bin/node
const list = require('./100-data').list;
if (list) {
  const array2 = list.map(function (num, index) {
    return num * index;
  });
  console.log(list);
  console.log(array2);
}
