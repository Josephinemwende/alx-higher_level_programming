#!/usr/bin/node
const [arg] = process.argv.slice(2);
const y = 'C is fun';
if (isNaN(arg)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log(y);
  }
}
