#!/usr/bin/node
const length = parseInt(process.argv[2], 10);
if (isNaN(length)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < length; i++) {
  console.log('C is fun');
}
