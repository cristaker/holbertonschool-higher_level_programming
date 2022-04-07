#!/usr/bin/node
const fs = require('fs');

const FaArg = fs.readFileSync(process.argv[2]).toString();
const FbArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], FaArg + FbArg);
