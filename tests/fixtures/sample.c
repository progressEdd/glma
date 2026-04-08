#include <stdio.h>

/* A standalone function */
int add(int a, int b) {
    return a + b;
}

struct Point {
    int x;
    int y;
};

typedef struct {
    float width;
    float height;
} Rectangle;

int main() {
    struct Point p = {1, 2};
    return add(p.x, p.y);
}
