#!/usr/bin/node

const n = Number(process.argv[2]);
if (n >= 0) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else if (isNaN(n)) {
  console.log('Missing size');
}
