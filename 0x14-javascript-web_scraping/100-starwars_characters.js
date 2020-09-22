#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const characters = JSON.parse(body).characters;
  characters.forEach((currentItem) => {
    request(currentItem, function (error, response, body) {
      if (error) console.error('error:', error);
      console.log(JSON.parse(body).name);
    });
  });
});
