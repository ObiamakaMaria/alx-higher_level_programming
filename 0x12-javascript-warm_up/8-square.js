#!/usr/bin/node

const size = parseInt(process.argv[2], 10);

if (!isNaN(size)) {
  for (let b = 0; b < size; b++) {
    let line = '';
    for (let c = 0; c < size; c++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
