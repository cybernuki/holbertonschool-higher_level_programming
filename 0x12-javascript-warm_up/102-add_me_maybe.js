#!/usr/bin/node
// Author: Cybernuki
// this function increments and calls a function.

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
