#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
