#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  const arg2 = argv[2];
  console.log(arg2);
}
