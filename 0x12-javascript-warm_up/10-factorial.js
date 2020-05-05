#!/usr/bin/node
// Author: Cybernuki
// This script computes and prints a factorial

function factorial(a) {
        if (isNaN(a) || a == '1' || !a) {
                return(1);
        }
        return(factorial(a - 1) * a);
}

const arg = parseInt(process.argv[2]);

console.log(factorial(arg));
