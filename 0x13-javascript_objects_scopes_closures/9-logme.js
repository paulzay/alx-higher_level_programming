#!/usr/bin/node

exports.logMe = function (item) {
  let printed = 0;
  console.log(`${printed}: ${item}`);
  printed += 1;
};
