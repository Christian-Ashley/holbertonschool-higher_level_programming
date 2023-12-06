#!/usr/bin/node
const process = require('process');
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(path, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});