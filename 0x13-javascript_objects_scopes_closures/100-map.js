#!/usr/bin/node

const list = require('./100-data.js');
const arr = [];
list.map((num, index) => {
  arr.push(num * index);
});
console.log(list);
console.log(arr);
