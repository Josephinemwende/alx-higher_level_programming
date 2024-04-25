#!/usr/bin/node

const [arg] = process.argv.slice(2);
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return (1);
  }
  return (n * factorial(n -1));
}
const result = factorial(parseInt(arg));
console.log(result);
