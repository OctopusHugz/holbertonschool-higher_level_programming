#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
}
const newArr = process.argv.slice(2, process.argv.length);
newArr.sort().reverse().shift();
console.log(Math.max(...newArr));
