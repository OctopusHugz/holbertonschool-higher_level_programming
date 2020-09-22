#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  try {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach((currentItem) => {
      currentItem.characters.forEach((currentItem) => {
        if (currentItem === 'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      });
    });
    console.log(count);
  } catch (error) {}
});
