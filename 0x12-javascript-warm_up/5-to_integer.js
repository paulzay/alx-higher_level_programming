#!/usr/bin/node

const { argv } = require('node:process');

if (isNaN(parseInt(argv[2], 10))) {
  console.log('My number: ' + parseInt(argv[2], 10));
} else {
  console.log('Not a number');
}
