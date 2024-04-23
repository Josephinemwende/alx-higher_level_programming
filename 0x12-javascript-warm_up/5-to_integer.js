#!/usr/bin/node
const [arg] = process.argv.slice(2);
if (!isNaN(arg)) {
  console.log('My number: ' + parseInt(arg));
} else {
  console.log('Not a number');
}
