#!/usr/bin/node
// Author: Cybernuki
// This script prints My number: <first argument converted in integer> 
// if the first argument can be converted to an integer:

const arg_1 = parseInt(process.argv[2]);

if (isNaN(arg_1)) {
        console.log('Not a number');
}
else {
        console.log(arg_1);
}