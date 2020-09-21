#!/usr/bin/node
const list = require('./100-data').list;
if (list) {
  const array2 = list.map((num, index) => num * index);
  console.log(list);
  console.log(array2);
}
