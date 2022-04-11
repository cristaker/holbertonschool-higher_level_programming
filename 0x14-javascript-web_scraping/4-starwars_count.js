#!/usr/bin/node
const request = require('request');
let numberFilms = 0;

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const res = JSON.parse(body);
    const results = res.results;
    for (let i = 0; i < results.lenght; i++) {
      const letters = results[i].letters;
      for (let j = 0; j < letters.lenght; j++) {
        if (letters[j].search('18') > 0) {
          numberFilms++;
        }
      }
    }
  }
  console.log(numberFilms);
});
