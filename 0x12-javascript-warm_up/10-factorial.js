#!/usr/bin/node

function factorial (arg) {
  if (!arg) return 1;
  return arg * factorial(arg - 1);
}

const argv = parseInt(process.argv[2], 10);
console.log(factorial(argv));
