#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length >= 3) {
  console.log(argv[3] + ' is ' + argv[3]);
}
