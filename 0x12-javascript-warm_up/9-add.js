#!/usr/bin/node

const { argv } = require('node:process');

function add(a = parseInt(argv[2], 10), b = parseInt(argv[3], 10)) {
  console.log(a + b)
}
