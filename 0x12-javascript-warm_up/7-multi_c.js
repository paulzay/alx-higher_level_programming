#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argv[2]; i += 1) {
    console.log('C is fun');
  }
}
