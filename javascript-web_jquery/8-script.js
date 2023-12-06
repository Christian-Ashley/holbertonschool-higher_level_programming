#!/usr/bin/node
// Write a JavaScript script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let i = 0; i < data.results.length; i++) {
    $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
}
);