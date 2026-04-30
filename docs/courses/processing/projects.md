---
tags:
  - processing
  - generative-art
  - creative-coding
  - projects
  - java
  - course
---

# Processing — Projects

## Project 1: Point Scatter (Zay Legend)

### What It Does

7,500 gold points wander randomly across a 300x300 canvas. Each point moves in a small random direction each frame and wraps around to the opposite edge when it goes out of bounds. The text "Zay Legend" is drawn in the center of the canvas.

### How It Works

- Arrays store the `x`, `y`, and RGB color values for each of the 7,500 points
- `setup()` initializes all points at random positions and sets their color to gold (255, 215, 0)
- `draw()` moves each point by a random offset between -1 and 1 on both axes
- Edge wrapping: if a point goes past any edge, it reappears on the opposite side
- `frameRate(1000)` runs as fast as possible, creating a fast particle effect

### Code

```java
int count = 7500;

float[] x = new float[count];
float[] y = new float[count];
float[] r = new float[count];
float[] g = new float[count];
float[] b = new float[count];

void setup() {
  size(300, 300);
  for (int i = 0; i < count; i++) {
    x[i] = random(width);
    y[i] = random(height);
    r[i] = 255;
    g[i] = 215;
    b[i] = 0;
  }
  background(200);
  noSmooth();
  frameRate(1000);
}

void draw() {
  for (int i = 0; i < count; i++) {
    x[i] += random(-1, 1);
    y[i] += random(-1, 1);
    if (x[i] < 0) x[i] = width;
    if (x[i] > width) x[i] = 0;
    if (y[i] < 0) y[i] = height;
    if (y[i] > height) y[i] = 0;
    stroke(r[i], g[i], b[i]);
    point(x[i], y[i]);
    text("Zay Legend", 100, 100, 100);
  }
}
```

---

## Project 2: Interactive Spirograph

### What It Does

Draws a spirograph pattern that updates in real time based on mouse position. Moving the mouse changes the shape of the pattern by controlling the inner radius (`r2`) and point distance (`h`). Keyboard controls let you adjust drawing speed and pause the animation.

**Controls:**
- **Mouse X/Y:** Change spirograph shape (inner radius and point distance)
- **Keys 1–9:** Change drawing speed (1 = slowest, 9 = fastest)
- **Spacebar:** Pause/unpause

### How It Works

- The outer radius `r1` grows continuously, resetting to 0 when it exceeds half the canvas width
- Mouse X and Y are divided by 2 to produce `r2` and `h`, respectively
- A `SpiroCircle` class encapsulates the hypotrochoid math and handles drawing
- `drawIterations()` steps through 1,000 angle increments per frame, drawing a point at each
- Stroke color uses `sin(PI * i / iter) * 255` — a sine-wave grayscale gradient across the curve
- `strokeWeight(6)` makes each point visible and slightly overlapping for a smooth curve

### Code

```java
SpiroCircle sc;
float r1, incr;
boolean pause;

void setup() {
  size(400, 400);
  strokeWeight(25);
  smooth();
  sc = new SpiroCircle();
  r1 = 0.0;
  incr = 0.05;
  pause = false;
}

void draw() {
  r1 += incr;
  if (r1 > width / 2) r1 = 0.0;

  if (keyPressed) {
    if (key >= '1' && key <= '9')
      incr = ((int) key - '1' + 1) / 20.0;
    pause = (key == ' ');
  }

  if (!pause) {
    background(0);
    float mx = (mouseX == 0) ? 300 : mouseX;
    float my = (mouseY == 0) ? 300 : mouseY;
    sc.init(width/2, height/2, r1, mx/2, my/2);
    sc.drawIterations(1000, incr);
  }
}

class SpiroCircle {
  int cx, cy;
  float r1, r2, h;
  float prev_x, prev_y;
  boolean first;

  public void init(int x, int y, float radius_1, float radius_2, float point_distance) {
    cx = x; cy = y;
    r1 = radius_1; r2 = radius_2; h = point_distance;
    first = true;
  }

  public void drawIterations(int iter, float incr) {
    float rads = 0.0;
    for (int i = 0; i < iter; ++i) {
      stroke(sin(PI * i / iter) * 255 - 5);
      drawPoint(rads);
      rads += incr;
    }
  }

  private void drawPoint(float rads) {
    float x = cx + (r1 - r2) * cos(rads) + h * cos((r1 - r2) / r2 * rads);
    float y = cy + (r1 - r2) * sin(rads) + h * sin((r1 - r2) / r2 * rads);
    if (!first) { strokeWeight(6); point(x, y); }
    first = false;
    prev_x = x; prev_y = y;
  }
}
```

---

## Project 3: Gold Spirograph (Mouse-Controlled)

### What It Does

Identical structure to Project 2 but renders the spirograph in **solid gold** (RGB 255, 215, 0) rather than a sine-wave grayscale gradient. The canvas is wider (1000x500) to give the pattern more room to expand.

### How It Works

The core logic is the same as Project 2 — hypotrochoid equation, mouse-driven `r2` and `h`, growing `r1`. The key difference is in `drawIterations()`:

**Project 2 (sine gradient):**
```java
stroke(sin(PI * i / iter) * 255 - 5);
```

**Project 3 (solid gold):**
```java
stroke(255, 215, 0);
```

This small change produces a completely different visual character — a glowing, uniform gold curve instead of a shifting light-to-dark pattern.

### Code

```java
SpiroCircle sc;
float r1, incr;
boolean pause;

void setup() {
  size(1000, 500);
  strokeWeight(25);
  smooth();
  sc = new SpiroCircle();
  r1 = 0.0;
  incr = 0.05;
  pause = false;
}

void draw() {
  r1 += incr;
  if (r1 > width / 2) r1 = 0.0;

  if (keyPressed) {
    if (key >= '1' && key <= '9')
      incr = ((int) key - '1' + 1) / 20.0;
    pause = (key == ' ');
  }

  if (!pause) {
    background(0);
    float mx = (mouseX == 0) ? 300 : mouseX;
    float my = (mouseY == 0) ? 300 : mouseY;
    sc.init(width/2, height/2, r1, mx/2, my/2);
    sc.drawIterations(1000, incr);
  }
}

class SpiroCircle {
  int cx, cy;
  float r1, r2, h;
  float prev_x, prev_y;
  boolean first;

  public void init(int x, int y, float radius_1, float radius_2, float point_distance) {
    cx = x; cy = y;
    r1 = radius_1; r2 = radius_2; h = point_distance;
    first = true;
  }

  public void drawIterations(int iter, float incr) {
    float rads = 0.0;
    for (int i = 0; i < iter; ++i) {
      stroke(255, 215, 0);  // solid gold
      drawPoint(rads);
      rads += incr;
    }
  }

  private void drawPoint(float rads) {
    float x = cx + (r1 - r2) * cos(rads) + h * cos((r1 - r2) / r2 * rads);
    float y = cy + (r1 - r2) * sin(rads) + h * sin((r1 - r2) / r2 * rads);
    if (!first) { strokeWeight(6); point(x, y); }
    first = false;
    prev_x = x; prev_y = y;
  }
}
```

---

## Comparison: Projects 2 vs. 3

| Feature | Project 2 | Project 3 |
|---|---|---|
| Canvas size | 400x400 | 1000x500 |
| Stroke color | Sine-wave grayscale gradient | Solid gold (255, 215, 0) |
| Mouse control | Yes | Yes |
| Speed keys (1–9) | Yes | Yes |
| Spacebar pause | Yes | Yes |
| Core math | Hypotrochoid | Hypotrochoid (identical) |
