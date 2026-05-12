use std::collections::HashMap;

/// A point in 2D space
struct Point {
    x: f64,
    y: f64,
}

impl Point {
    fn new(x: f64, y: f64) -> Self {
        Self { x, y }
    }

    fn distance(&self) -> f64 {
        (self.x * self.x + self.y * self.y).sqrt()
    }
}

enum Shape {
    Circle(f64),
    Rectangle(f64, f64),
}

trait Describe {
    fn describe(&self) -> String;
}

impl Describe for Point {
    fn describe(&self) -> String {
        format!("Point({}, {})", self.x, self.y)
    }
}

fn main() {
    let p = Point::new(1.0, 2.0);
    println!("{}", p.describe());
}
