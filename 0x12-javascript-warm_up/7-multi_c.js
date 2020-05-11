#!/usr/bin/node
// Author: Cybernuki
// This script prints x times “C is fun”

const count = parseInt(process.argv[2]);

if (isNaN(count)) {
  console.log('Missing number of occurrence');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
