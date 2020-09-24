#!/usr/bin/node
const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const films = data.results;
  films.forEach((film) => {
    $('<li>' + film.title + '</li>').appendTo('ul#list_movies');
  });
});
