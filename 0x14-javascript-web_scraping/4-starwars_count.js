#!/usr/bin/node
const request = require('request');
const countarg = process.argv;
request(countarg[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let number = 0;
  const res = JSON.parse(body).results;
  for (let i = 0; i < res.length; i++) {
    const character = res[i].characters.find((res) => {
      return (res.match(/18/));
    });
    if (character !== undefined) {
      number++;
    }
  }
  console.log(number);
});
