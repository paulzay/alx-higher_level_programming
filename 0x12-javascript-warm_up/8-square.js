#!/usr/bin/node

const { argv } = require('node:process');
const size = parseInt(argv, 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= size; i++) {
    let row = '';
    for (let j = 1; j <= size; j++) row += 'X';
    console.log(row);
  }
}
