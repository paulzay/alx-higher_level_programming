#!/usr/bin/node

const { argv } = require('node:process');

if (typeof (argv[2]) === 'number') {
  console.log('My number: ' + argv[2])
} else {
  console.log('Not a number');
}
