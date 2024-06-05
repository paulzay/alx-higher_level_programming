#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');
const fs = require('fs');

request(argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  try {
    fs.writeFile(process.argv[3], body, 'utf8', function (err, result) {
      if (err) console.log(err);
    });
  } catch (err) {
    console.log(err);
  }
});
