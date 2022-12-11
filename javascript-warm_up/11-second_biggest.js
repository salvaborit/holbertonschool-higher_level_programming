#!/usr/bin/node

let args = process.argv.splice(2);

if (args.length === 0) return;

args.forEach((item, index) => {
  args[index] = parseInt(item);
});
args.sort((item, index) => item - index);

console.log(args[args.length - 2]);
