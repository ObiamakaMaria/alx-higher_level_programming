#!/usr/bin/node
/* imports a dictionary of occurrences by user id and computes
 * a dictionary of user ids by occurrence */
const dict = require('./101-data.js').dict;
const sortdic = {};
for (const key in dict) {
  if (sortdic[dict[key]] === undefined) {
    sortdic[dict[key]] = [key];
  } else {
    sortdic[dict[key]].push(key);
  }
}
console.log(sortdic);
