#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');

request(argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).results.filter((res) => {
    return res.characters.filter((url) => { return url.includes('18'); }).length;
  }).length);
});
