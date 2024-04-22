#!/usr/bin/node

const { argv } = require('node:process');

if (typeof(argv[2] !== 'number') {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[2]; i += 1) {
    console.log('X')
  }
}
