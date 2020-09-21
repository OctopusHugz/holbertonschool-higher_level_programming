#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], function (err, fd) {
  if (err) {
    return console.error(err);
  }
  fs.writeFile(process.argv[4], fd.toString(), { flag: 'a' }, function (err) {
    if (err) {
      return console.error(err);
    }
  });
});
fs.readFile(process.argv[3], function (err, fd) {
  if (err) {
    return console.error(err);
  }
  fs.writeFile(process.argv[4], fd.toString(), { flag: 'a' }, function (err) {
    if (err) {
      return console.error(err);
    }
  });
});
