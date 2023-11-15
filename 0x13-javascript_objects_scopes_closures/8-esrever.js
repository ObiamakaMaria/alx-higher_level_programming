#!/usr/bin/node
// This script returns the reversed version of a list
exports.esrever = function (list) {
  const len = Math.floor(list.length / 2);
  for (let a = 0; a < len; a++) {
    const lid = list.length - a - 1;
    const holder = list[lid];
    list[lid] = list[a];
    list[a] = holder;
  }
  return (list);
};
