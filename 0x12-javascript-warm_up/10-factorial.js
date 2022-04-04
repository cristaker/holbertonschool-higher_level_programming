#!/usr/bin/node

function fact (a) {
  if ((Number.isNaN(a)) || (a === 1)) {
    return 1;
  }
  return fact(a - 1) * a;
}

console.log(fact(parseInt(process.argv[2])));
