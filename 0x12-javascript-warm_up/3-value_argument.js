#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 2) {
  console.log('No argument');
} else {
  const arg1 = argv[2];
  console.log(arg1);
}