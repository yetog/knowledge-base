---
tags:
  - html
  - css
  - javascript
  - web
  - coding
  - course
---

# Web Fundamentals

## HTML

### What is HTML?

HTML (HyperText Markup Language) defines the structure and content of a web page. It uses tags to describe elements — headings, paragraphs, links, images, forms, and more.

### Basic Document Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Page Title</h1>
        <nav><a href="/home">Home</a></nav>
    </header>
    <main>
        <p>Hello, World!</p>
        <img src="image.jpg" alt="Description">
    </main>
</body>
</html>
```

### Common Tags

| Tag              | Purpose                                |
|------------------|----------------------------------------|
| `h1`–`h6`        | Headings (h1 = largest)               |
| `p`              | Paragraph                              |
| `a`              | Hyperlink — uses `href` attribute      |
| `img`            | Image — uses `src` and `alt`           |
| `div`            | Generic block container                |
| `span`           | Generic inline container               |
| `ul` / `ol`      | Unordered / ordered list               |
| `li`             | List item                              |
| `table`          | Table                                  |
| `tr` / `th` / `td` | Table row / header cell / data cell  |

### Attributes

Attributes are key-value pairs added inside an opening tag that modify element behavior.

| Attribute | Used on       | Purpose                          |
|-----------|---------------|----------------------------------|
| `href`    | `<a>`         | Link destination URL             |
| `src`     | `<img>`       | Image file path or URL           |
| `alt`     | `<img>`       | Accessible text description      |
| `class`   | Any element   | CSS class hook (reusable)        |
| `id`      | Any element   | Unique identifier for CSS / JS   |
| `style`   | Any element   | Inline CSS styling               |

### Semantic HTML

Semantic tags communicate meaning to browsers, search engines, and screen readers.

| Tag         | Meaning                              |
|-------------|--------------------------------------|
| `<header>`  | Page or section header               |
| `<nav>`     | Navigation links                     |
| `<main>`    | Primary content area                 |
| `<article>` | Self-contained piece of content      |
| `<section>` | Thematic grouping of content         |
| `<footer>`  | Page or section footer               |

### Forms

```html
<form action="/submit" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" placeholder="Your name">

    <label for="email">Email:</label>
    <input type="email" id="email" name="email">

    <button type="submit">Submit</button>
</form>
```

---

## CSS

### What is CSS?

CSS (Cascading Style Sheets) controls the visual presentation of HTML elements — colors, layout, spacing, fonts, and responsiveness.

### Selectors

```css
/* Element selector */
h1 { color: navy; }

/* Class selector */
.highlight { background: yellow; }

/* ID selector */
#header { font-size: 24px; }

/* Descendant selector */
nav a { text-decoration: none; }
```

### Box Model

Every element is a box. From inside out: **content → padding → border → margin**.

```css
.card {
    width: 300px;          /* content width */
    padding: 16px;         /* space inside border */
    border: 1px solid #ccc;
    margin: 24px;          /* space outside border */
}
```

### Flexbox

Flexbox provides one-dimensional layout control (row or column).

```css
.container {
    display: flex;
    justify-content: center;  /* horizontal alignment */
    align-items: center;      /* vertical alignment */
    gap: 16px;                /* space between children */
}
```

### Colors

```css
/* Hex */
color: #3a86ff;

/* RGB */
color: rgb(58, 134, 255);

/* HSL */
color: hsl(217, 100%, 61%);
```

### Media Queries (Responsive Design)

```css
/* Default: row layout */
.container {
    display: flex;
    flex-direction: row;
}

/* On screens 768px wide or less: stack vertically */
@media (max-width: 768px) {
    .container {
        flex-direction: column;
    }
}
```

---

## JavaScript

### What is JavaScript?

JavaScript is the programming language of the web. It adds interactivity and dynamic behavior to HTML/CSS pages — and runs in the browser without installation.

### Variables

```javascript
const name = "Isayah"; // block-scoped, immutable binding
let count = 0;         // block-scoped, reassignable
var old = "avoid";     // function-scoped (legacy)
```

### Data Types

| Type        | Example               |
|-------------|-----------------------|
| `string`    | `"hello"`             |
| `number`    | `42`, `3.14`          |
| `boolean`   | `true`, `false`       |
| `null`      | `null`                |
| `undefined` | variable declared but not assigned |
| `object`    | `{ key: "value" }`   |
| `array`     | `[1, 2, 3]`           |

### Functions

```javascript
// Function declaration
function greet(name) {
    return `Hello, ${name}!`;
}

// Function expression
const double = function(n) { return n * 2; };

// Arrow function (concise)
const greet = (name) => `Hello, ${name}!`;
```

### DOM Manipulation

```javascript
// Select an element
const btn = document.querySelector('#myBtn');
const heading = document.querySelector('h1');

// Modify content
heading.textContent = 'Updated Title';
heading.style.color = 'red';

// Add/remove CSS classes
heading.classList.add('active');
heading.classList.remove('active');
```

### Events

```javascript
btn.addEventListener('click', () => {
    document.querySelector('#output').textContent = 'Clicked!';
});

// Common event types
// 'click'    — mouse click
// 'keydown'  — keyboard key pressed
// 'submit'   — form submission
// 'input'    — input field value changed
```

### Async JavaScript

JavaScript is single-threaded. Async patterns let it wait for slow operations (network, file I/O) without blocking.

```javascript
// Callbacks (old style)
setTimeout(() => console.log("Done"), 1000);

// Promises
fetch('https://api.example.com/data')
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));

// Async/Await (modern, preferred)
async function getData() {
    try {
        const res = await fetch('https://api.example.com/data');
        const data = await res.json();
        return data;
    } catch (err) {
        console.error('Fetch failed:', err);
    }
}
```

### Fetch API

```javascript
// GET request
async function getUser(id) {
    const res = await fetch(`/api/users/${id}`);
    const user = await res.json();
    console.log(user);
}

// POST request
async function createUser(userData) {
    const res = await fetch('/api/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData)
    });
    return await res.json();
}
```
