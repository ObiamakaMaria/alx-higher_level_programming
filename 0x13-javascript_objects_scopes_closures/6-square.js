#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c = 'X') {
    for (let x = 0; x < this.height; x++) {
      let row = '';
      for (let y = 0; y < this.width; y++) {
        row += c;
      }
      console.log(row);
    }
  }
};
