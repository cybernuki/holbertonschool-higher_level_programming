#!/usr/bin/node
// Author: Cybernuki
// This script prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer:

const arg1 = parseInt(process.argv[2]);

if (isNaN(arg1)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${arg1}`);
}
