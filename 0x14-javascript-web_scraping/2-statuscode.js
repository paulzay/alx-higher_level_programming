#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');

request(argv[2], function (error, response) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response && response.statusCode);
});
