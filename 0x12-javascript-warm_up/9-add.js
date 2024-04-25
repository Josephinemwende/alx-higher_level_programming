#!/usr/bin/node
const [arg1, arg2] = process.argv.slice(2);

function add (a, b) {
  return a + b;
}
const result = add(parseInt(arg1), parseInt(arg2));
console.log(result);
