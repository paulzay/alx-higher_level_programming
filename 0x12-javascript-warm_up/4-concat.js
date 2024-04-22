#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length >= 3) {
  console.log(argv[1] + ' is ' argv[2]);
}
