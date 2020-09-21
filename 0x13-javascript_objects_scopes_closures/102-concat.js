#!/usr/bin/node
const concat = require('concat-files');
concat([process.argv[2], process.argv[3]], process.argv[4], function (err) {
  if (err) throw err;
  console.log('done');
});

// const fs = require('fs');
// const file1 = fs.open(process.argv[2], 'r', function (err, fd) {
//   if (err) {
//     return console.error(err);
//   }
// });
// const file2 = fs.readFile(process.argv[3]);
// console.log(file1);
