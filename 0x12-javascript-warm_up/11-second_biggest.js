#!/usr/bin/node
// Author: Cybernuki
// This script searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2);

if (args.length < 2) {
        console.log('0');
}
else {
        args.sort((a, b)  => {
                return b - a;
              });
        console.log(args[1]);
}
