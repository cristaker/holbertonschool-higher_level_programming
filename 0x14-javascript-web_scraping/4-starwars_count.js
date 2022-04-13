#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  let numberFilms = 0;
  const res = JSON.parse(body).results;
  for (let i = 0; i < res.length; i++) {
    const result = res[i].result.find((res) => {
      return (res.match(/18/));
    });
    if (result !== undefined) {
      numberFilms++;
    }
  }
  console.log(numberFilms);
});
