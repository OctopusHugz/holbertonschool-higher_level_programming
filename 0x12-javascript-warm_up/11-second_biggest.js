#!/usr/bin/node
const length = process.argv.length;
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const newArr = process.argv.slice(2, length);
  newArr.sort((a, b) => a - b);
  newArr.pop();
  console.log(Math.max(...newArr));
}
// } else {
//   const newArr = process.argv.slice(2, length);
//   newArr.sort();
//   if (parseInt(newArr[newArr.length - 1], 10) > parseInt(newArr[0], 10)) {
//     newArr.reverse();
//   }
//   newArr.shift();
//   console.log(Math.max(...newArr));
// }
