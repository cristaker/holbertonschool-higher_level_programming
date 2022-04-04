#!/usr/bin/node

const i = parseInt(process.argv[2]);
if (Number.isNaN(i)) {
  console.log('Missing size');
} else {
  for (let a = 0, s; a < i; a++) {
    s = '';
    for (let b = 0; b < i; b++) {
      s += 'X';
    }
    console.log(s);
  }
}
