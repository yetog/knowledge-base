---
tags:
  - processing
  - generative-art
  - creative-coding
  - java
  - course
---

# Processing — Creative Coding

## What is Processing?

Processing is an open-source language and IDE built on top of Java, designed for visual artists, designers, and learners exploring creative coding. It is widely used for generative art, data visualization, interactive sketches, and animation.

- **Website:** [processing.org](https://processing.org)
- **Language base:** Java (with a simplified syntax layer)
- A single Processing program is called a **sketch**

---

## Core Structure

Every Processing sketch is built around two main functions:

```java
void setup() {
  // Runs once when the sketch starts
  // Use for initialization: canvas size, colors, starting values
}

void draw() {
  // Loops continuously (~60fps by default)
  // Use for animation, input response, drawing updates
}
```

---

## Canvas and Drawing

### Setting Up the Canvas

```java
size(400, 400);  // width x height in pixels
```

### Basic Shapes

All shapes are positioned using `x, y` coordinates from the top-left corner.

```java
ellipse(x, y, w, h);   // circle/oval — x,y is center
rect(x, y, w, h);      // rectangle — x,y is top-left corner
line(x1, y1, x2, y2);  // line between two points
point(x, y);           // single pixel
```

### Color

```java
background(200);            // gray background (0=black, 255=white)
background(0);              // black background
stroke(255, 0, 0);          // red outline (RGB)
stroke(255, 215, 0);        // gold outline
fill(255, 215, 0);          // gold fill
noStroke();                 // remove outline
noFill();                   // remove fill
```

Colors use **RGB** values from 0–255. A single value is treated as grayscale.

---

## Animation

```java
frameRate(60);   // default; set lower to slow animation
```

The `draw()` loop runs at the set frame rate. To animate, update variable values each frame and redraw shapes.

```java
float x = 0;

void draw() {
  background(0);     // clear canvas each frame
  ellipse(x, 200, 20, 20);
  x += 2;           // move right each frame
}
```

---

## Input

### Mouse

```java
mouseX   // current cursor X position
mouseY   // current cursor Y position
mousePressed  // boolean: true if mouse button is held
```

### Keyboard

```java
keyPressed   // boolean: true if any key is held
key          // the character of the key currently pressed
```

Example — check which key is held:

```java
if (keyPressed) {
  if (key == ' ') {
    // spacebar logic
  }
  if (key >= '1' && key <= '9') {
    // number key logic
  }
}
```

---

## Math Utilities

```java
random(min, max)    // random float between min and max
sin(angle)          // sine of angle (in radians)
cos(angle)          // cosine of angle (in radians)
PI                  // constant ~3.14159
```

### Circular Motion

Using `sin()` and `cos()` with an incrementing angle creates circular or oscillating motion:

```java
float t = 0;

void draw() {
  float x = cx + radius * cos(t);
  float y = cy + radius * sin(t);
  point(x, y);
  t += 0.05;
}
```

---

## Spirograph Math

Processing is well-suited for parametric curves. The **hypotrochoid** equation is the mathematical basis for spirograph patterns:

```
x = (r1 - r2) * cos(t) + h * cos((r1 - r2) / r2 * t)
y = (r1 - r2) * sin(t) + h * sin((r1 - r2) / r2 * t)
```

**Parameters:**

| Variable | Meaning |
|---|---|
| `r1` | Outer (fixed) circle radius |
| `r2` | Inner (rolling) circle radius |
| `h` | Distance from the center of the inner circle to the drawing point |
| `t` | Angle parameter (increments over time) |

Varying `r2` and `h` produces dramatically different petal and loop patterns. When `r1 / r2` is a whole number ratio, the curve closes into a perfect loop.

---

## Classes in Processing

Processing supports Java-style classes, useful for encapsulating sketch objects:

```java
class SpiroCircle {
  int cx, cy;
  float r1, r2, h;

  public void init(int x, int y, float radius_1, float radius_2, float point_dist) {
    cx = x; cy = y;
    r1 = radius_1; r2 = radius_2; h = point_dist;
  }

  public void drawPoint(float rads) {
    float x = cx + (r1 - r2) * cos(rads) + h * cos((r1 - r2) / r2 * rads);
    float y = cy + (r1 - r2) * sin(rads) + h * sin((r1 - r2) / r2 * rads);
    point(x, y);
  }
}
```

Instantiate with `SpiroCircle sc = new SpiroCircle();` and call methods normally.
