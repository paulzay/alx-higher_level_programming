#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length == 1) {
  console.log('No argument');
} else {
  const arg1 = argv[1];
  console.log(arg1);
}
