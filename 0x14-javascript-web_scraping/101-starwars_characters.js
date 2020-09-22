#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
function getCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      resolve(body);
    });
  });
}

async function printFunc (url) {
  const body = await getCharacter(url);
  console.log(JSON.parse(body).name);
}
request(url, async function (error, response, body) {
  if (error) console.error('error:', error);
  const characters = JSON.parse(body).characters;
  for (let index = 0; index < characters.length; index++) {
    const characterUrl = characters[index];
    await printFunc(characterUrl);
  }
  //   characters.forEach(async (characterUrl) => printFunc(characterUrl));
});
// function printFunc (body) {
//   console.log(JSON.parse(body).name);
// }
// const characters = request(url, function (error, response, body) {
//   if (error) console.log('error:', error);
//   console.log(JSON.parse(body));
//   characters.forEach((characterUrl) => {
//     request(characterUrl, printFunc(body));
//   });
//   return JSON.parse(body).characters;
// });
// console.log(characters);
