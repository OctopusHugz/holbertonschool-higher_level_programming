#!/usr/bin/node
const list = require('./100-data').list;
if (list.length > 0) {
  const array2 = list.map((x) => x * list.indexOf(x));
  console.log(list);
  console.log(array2);
}
