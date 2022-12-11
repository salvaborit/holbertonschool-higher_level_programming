#!/usr/bin/node

const args = process.argv.splice(2);

if (args.length === 0) {
    console.log(0);
    return;
};

args.forEach((item, index) => {
  if (item[0] == '-') {
    console.log(0);
    process.exit();
  }
  args[index] = parseInt(item);
});
args.sort((item, index) => item - index);

console.log(args[args.length - 2]);
