#!/usr/bin/node
const dict = require('./101-data').dict;
const nD = {};

Object.keys(dict).map(function (key, index) {
  if (nD[dict[key]] === undefined) {
    nD[dict[key]] = [];
  }
  nD[dict[key]].push(key);
});

console.log(nD);
