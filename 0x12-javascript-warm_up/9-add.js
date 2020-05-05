#!/usr/bin/node
// Author: Cybernuki
// This script prints the addition of 2 integers

function add(a, b) {
        return (a + b)
}

const arg_1 = parseInt(process.argv[2]);
const arg_2 = parseInt(process.argv[3]);

console.log(add(arg_1, arg_2));
