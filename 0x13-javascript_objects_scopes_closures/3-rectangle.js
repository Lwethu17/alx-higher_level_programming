#!/usr/bin/node

class Rectangle {
	constructor (a, b) {
		if (a >= 1 && b >= 1) {
			this.weight = a;
			this.height = b;
		}
	}

	print () {
		const character = 'X';
		for (let i = 0; i < this.height; i++) {
			console.log(character.repeat(this.width));
		}
	}
}

module.exports = Rectangle;
