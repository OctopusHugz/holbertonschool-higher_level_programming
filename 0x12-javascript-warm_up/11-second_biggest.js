#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const newArr = process.argv.slice(2, process.argv.length);
  newArr.sort((a, b) => a - b);
  newArr.pop();
  console.log(Math.max(...newArr));
}
