#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], { encoding: 'utf-8' }, function (err, fd) {
  if (err) {
    return console.log(err);
  }
  console.log(fd.toString());
});
