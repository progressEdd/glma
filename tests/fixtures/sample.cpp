#include <vector>
#include <string>

using namespace std;

namespace MyApp {

/* A standalone function */
int add(int a, int b) {
    return a + b;
}

class Shape {
public:
    virtual double area() = 0;
    virtual ~Shape() {}
};

class Rectangle : public Shape {
    double width;
    double height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    ~Rectangle() override = default;
    double area() override { return width * height; }
};

template <typename T>
T max_value(T a, T b) {
    return (a > b) ? a : b;
}

struct Point {
    double x;
    double y;
};

}
