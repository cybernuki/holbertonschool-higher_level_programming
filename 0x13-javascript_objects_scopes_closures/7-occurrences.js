#!/usr/bin/node
// This module finds number of occurrences

exports.nbOccurences = function (list, searchElement) {
  return list.filter(function (el) {
    return (el === searchElement);
  }).length;
};
