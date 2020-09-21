#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((currentItem) => {
    if (currentItem === searchElement) {
      count++;
    }
  });
  return count;
};
