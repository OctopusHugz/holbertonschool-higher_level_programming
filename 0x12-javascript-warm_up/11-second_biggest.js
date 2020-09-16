#!/usr/bin/node
const length = process.argv.length;
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const newArr = process.argv.slice(2, length);
  newArr.sort();
  if (parseInt(newArr[newArr.length - 1], 10) > parseInt(newArr[0], 10)) {
    newArr.reverse();
  }
  const shifted = newArr.shift();
  while (newArr[0] === shifted) {
    newArr.shift();
  }
  console.log(Math.max(...newArr));
}
