#!/usr/bin/node
//same as 1 but with protections against wierd shit

class Rectangle {
    constructor (w, h) {
      if (w >= 1 && h >= 1) {
        this.width = w;
        this.height = h;
      }
    }
  }
  
  module.exports = Rectangle;