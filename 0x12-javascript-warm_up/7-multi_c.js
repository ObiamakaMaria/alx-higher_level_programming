#!/usr/bin/node

const x = parseInt(process.argv[2], 10);

if (!isNaN(x)) {
  for (let n = 0; n < x; n++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
