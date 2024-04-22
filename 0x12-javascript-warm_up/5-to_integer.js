#!/usr/bin/node

const { argv } = require('node:process');

if (typeof (argv[2]) === 'number') {
  console.log('My number: ' + parseInt(argv[2]))
} else {
  console.log('Not a number');
}
