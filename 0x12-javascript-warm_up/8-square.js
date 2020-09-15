#!/usr/bin/node
const size = parseInt(process.argv[2], 10);
const arr = [];
if (isNaN(size)) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  arr.push('X');
}
for (let j = 0; j < size; j++) {
  console.log(arr.join(''));
}
