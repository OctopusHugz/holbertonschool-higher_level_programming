#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (
  error,
  response,
  body
) {
  if (error) console.error('error:', error);
  const characters = JSON.parse(body).characters;
  characters.forEach((currentItem) => {
    request(currentItem, function (error, response, body) {
      if (error) console.error('error:', error);
      console.log(JSON.parse(body).name);
    });
  });
});
