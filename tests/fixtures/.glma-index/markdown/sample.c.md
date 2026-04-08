# sample.c

*(File summary not yet generated — available after Phase 3.)*

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| add | function | A standalone function |
| Point | class |  |
| typedef struct { | class |  |
| main | function |  |

## Chunks

### add (function, L4-L6)

/* A standalone function */

```c
int add(int a, int b) {
    return a + b;
}
```

### Point (class, L8-L11)

```c
struct Point {
    int x;
    int y;
}
```

### typedef struct { (class, L13-L16)

```c
typedef struct {
    float width;
    float height;
} Rectangle;
```

### main (function, L18-L21)

```c
int main() {
    struct Point p = {1, 2};
    return add(p.x, p.y);
}
```
