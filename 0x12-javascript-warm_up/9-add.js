#!/usr/bin/node

const { argv } = require('node:process');

function add(a = argv[2], b = argv[3]) {
  console.log(a + b)
}
