#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) return console.log(error);
  const films = JSON.parse(body).results;
  let count = 0;
  films.forEach((film) => {
    film.characters.forEach((character) => {
      if (character === 'https://swapi-api.hbtn.io/api/people/18/') {
        count++;
      }
    });
  });
  console.log(count);
});
