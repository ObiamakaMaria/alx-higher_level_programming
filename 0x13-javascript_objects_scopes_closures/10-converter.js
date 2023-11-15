#!/usr/bin/node
// The script converts from base 10 to another base
exports.converter = function (base) {
  return function (num) {
    return (num.toString(base));
  };
};
