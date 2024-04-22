#!/usr/bin/node

const { argv } = require('node:process');

if (typeof(argv[1]) === 'number') {
  console.log()
} else {
  console.log('Not a number');
}
