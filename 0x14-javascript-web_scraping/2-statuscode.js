#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');

request(argv[2], function (error, response, body) {
  console.error('error: ', error);
  console.log('code: ', response && response.statusCode);
});
