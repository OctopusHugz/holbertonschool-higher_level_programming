#!/usr/bin/node
const res = parseInt(process.argv[2], 10);
if (isNaN(res)) {
  console.log('Not a number');
} else {
  console.log(res);
}
