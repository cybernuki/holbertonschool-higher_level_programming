#!/usr/bin/node
// Author: Cybernuki
// This script interpretates the argv

if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
