#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const donetasks = {};
request(url, (error, response, body) => {
  if (!error) {
    const reslt = JSON.parse(body);
    for (let i = 0; i < reslt.length; i++) {
      if (reslt[i].completed === true) {
        if (donetasks[reslt[i].userId] === undefined) {
          donetasks[reslt[i].userId] = 1;
        } else {
          donetasks[reslt[i].userId]++;
        }
      }
    }
    console.log(donetasks);
  } else {
    console.log(error);
  }
});
