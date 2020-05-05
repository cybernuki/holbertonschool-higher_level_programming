#!/usr/bin/node
// Author: Cybernuki
// This script interpretates the argv

if (process.argv.length === 2) {
  console.log('Argument found');
} else if (process.argv.lenght > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
