#!/usr/bin/node

class Rectangle {
	constructer (a, b) {
		if (a > 0 && b > 0) {
			this.width = a;
			this.height = b;
		}
	}

	print () {
		for (let i = 0; i < this.height; i++) {
			console.log('X'.repeat(this.width));

		}
	}

	rotate () {
		const aux = this.height;
		this.height = this.width;
		this.width = aux;
	}

	double () {
		this.height *= 2;
		this.width *= 2;
	}
}

module.exports = Rectangle;
