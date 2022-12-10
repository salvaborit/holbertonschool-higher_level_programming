#!/usr/bin/node

const n = parseInt(process.argv[2]);

if (n >= 0) {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
} else if (n === undefined) {
  console.log('Missing number of occurrences');
}
