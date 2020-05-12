#!/usr/bin/node
exports.converter = function (base) {
  return function convertNumber (number) {
    return number.toString(base);
  };
};
