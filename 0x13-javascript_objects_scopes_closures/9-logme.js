#!/usr/bin/node
/* The script prints the number of arguments already 
   printed and the new argument value */
let arg = 0;
exports.logMe = function (item) {
  console.log(`${arg++}: ${item}`);
};
