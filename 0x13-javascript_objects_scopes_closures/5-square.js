#!/usr/bin/node
/* This class  defines a square  class and inherits
   from Rectangle of 4-rectangle.js */
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
