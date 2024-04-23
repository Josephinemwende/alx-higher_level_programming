#!/usr/bin/node
const [arg] = process.argv.slice(2);
if (arg !== undefined) {
  console.log(arg);
} else {
  console.log('No argument');
}
