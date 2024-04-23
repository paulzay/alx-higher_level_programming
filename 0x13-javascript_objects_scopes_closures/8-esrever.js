#!/usr/bin/node

exports.esrever = function (list) {
  const reverseArray = [];
  for (let i = list.length - 1; i >= 0; i -= 1) {
    reverseArray.push(list[i]);
  }
  return reverseArray;
};
