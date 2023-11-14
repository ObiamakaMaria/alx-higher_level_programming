#!/usr/bin/node
/* There are three instances of this class
 * The print instance rints the rectangle using the character X
 * The rotate instance exchanges the width and the height of
 * the rectangle
 * The double instance multiples the width and the height
 * of the rectangle by 2
 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let row = '';
      for (let y = 0; y < this.width; y++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const a = this.height;
    this.height = this.width;
    this.width = a;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
};
