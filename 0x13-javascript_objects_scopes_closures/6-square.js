#!/usr/bin/node
// This module defines a square class

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const char = (c) || 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
