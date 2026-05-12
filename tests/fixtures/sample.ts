import { User } from './user';
import type { Config } from './config';

interface Shape {
    area(): number;
}

type Point = {
    x: number;
    y: number;
};

enum Color {
    Red,
    Green,
    Blue
}

class Circle implements Shape {
    constructor(private radius: number) {}

    area(): number {
        return Math.PI * this.radius * this.radius;
    }
}

class Square extends Shape {
    constructor(private size: number) {
        super();
    }
}

function greet(name: string): string {
    return `Hello, ${name}`;
}
