#!/usr/bin/node
const [arg] = process.argv.slice(2);

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  const size = parseInt(arg);
  for (let i = 0; i < size; i++) {
    let x = '';
    for (let j = 0; j < size; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
