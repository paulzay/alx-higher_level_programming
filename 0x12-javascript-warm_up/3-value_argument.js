#!/usr/bin/node

const { argv } = require('node:process');

if (!argv[3]) {
  console.log('No argument');
} else {
  const arg3 = argv[3];
  console.log(arg3);
}
