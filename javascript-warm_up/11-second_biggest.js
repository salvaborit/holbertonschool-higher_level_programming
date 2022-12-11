#!/usr/bin/node

const args = process.argv.splice(2);

if (args.length < 2) {
  console.log(0);
  process.exit();
}

args.forEach((item, index) => {
  args[index] = parseInt(item);
});
args.sort((item, index) => item - index);

console.log(args[args.length - 2]);
