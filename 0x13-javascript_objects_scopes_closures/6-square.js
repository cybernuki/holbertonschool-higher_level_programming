#!/usr/bin/node
// This module defines a square class

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    const char = (c) || 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
