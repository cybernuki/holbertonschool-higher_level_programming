#!/usr/bin/node
// This module reverse a list

exports.esrever = function (list) {
  const inverted = [];
  for (let i = list.length - 1; i >= 0; i--) {
    inverted.push(list[i]);
  }
  return inverted;
};
