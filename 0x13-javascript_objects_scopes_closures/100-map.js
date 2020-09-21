#!/usr/bin/node
const list = require('./100-data').list;
// const array2 = list.map((x) => x * list.indexOf(x));
const array2 = list.map(function (num, index) {
  return parseInt(num * index);
});
console.log(list);
console.log(array2);
// array2.forEach(currentItem => {
//   if (Object.is(array2[currentItem], -0)) {
//     array2[currentItem] = 0;
//   }
// });
// console.log(array2);
