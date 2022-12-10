#!/usr/bin/node

isNaN(parseInt(process.argv[2])) ? console.log('Not a number') : console.log('My number:', parseInt(process.argv[2]));
