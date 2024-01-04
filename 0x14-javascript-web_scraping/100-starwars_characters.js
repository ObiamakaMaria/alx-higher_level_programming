#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const result = JSON.parse(body);
  const actors = result.characters;
  for (let i = 0; i < actors.length; i++) {
    request.get(actors[i], (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const result = JSON.parse(body);
      console.log(result.name);
    });
  }
});
