#!/usr/bin/node
// Author: Cybernuki
// This script prints a square

const count = parseInt(process.argv[2]);

if (isNaN(count)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < count; i++) {
    console.log('#'.repeat(count));
  }
}
