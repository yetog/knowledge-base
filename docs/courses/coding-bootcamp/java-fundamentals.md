---
tags:
  - coding
  - java
  - course
---

# Java Fundamentals

## Lesson 1 — Introduction to Java

### What is Java?

Java is a general-purpose, object-oriented programming language created by Sun Microsystems in 1995. Its defining feature is platform independence: Java source code compiles to bytecode that runs on any machine with a JVM (Java Virtual Machine) installed.

**Analogy:** A class is a blueprint for a house; compilation is the process of building the house from that blueprint. Once compiled, the bytecode can be "built" (run) anywhere a JVM exists.

### Compilation Process

```
Source file (.java) → Java Compiler (javac) → Bytecode (.class) → JVM → Execution
```

### Data Types

| Type      | Example            | Notes                        |
|-----------|--------------------|------------------------------|
| `int`     | `int age = 25;`    | Whole numbers                |
| `double`  | `double price = 9.99;` | Decimal numbers          |
| `boolean` | `boolean isActive = true;` | true / false       |
| `String`  | `String name = "Isayah";` | Text (object type)  |
| `char`    | `char grade = 'A';` | Single character            |

### Operators

- **Arithmetic:** `+`, `-`, `*`, `/`, `%`
- **Comparison:** `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical:** `&&` (AND), `||` (OR), `!` (NOT)

### Hello World

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### Data Types Example

```java
int age = 25;
double price = 9.99;
boolean isActive = true;
String name = "Isayah";
```

### Control Flow

```java
// If / else
if (age >= 18) {
    System.out.println("Adult");
} else {
    System.out.println("Minor");
}

// For loop
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// While loop
int x = 0;
while (x < 10) {
    x++;
}

// Do-while loop
int y = 0;
do {
    y++;
} while (y < 5);
```

### OOP Core Concepts

| Concept       | Description                                              |
|---------------|----------------------------------------------------------|
| Class         | Blueprint that defines fields and methods                |
| Object        | An instance of a class                                   |
| Inheritance   | A subclass inherits fields and methods from a superclass |
| Encapsulation | Hiding internal state; exposing via public methods       |
| Polymorphism  | One interface, many implementations                      |

---

## Lesson 2 — Data Handling and Functions

### Arrays

```java
// Single-dimensional array
int[] shoppingList = {1, 2, 3, 4, 5};

// Access element
System.out.println(shoppingList[0]); // 1

// Multidimensional array
int[][] grades = {
    {100, 90, 80},
    {95, 85, 75}
};

// Access element
System.out.println(grades[0][1]); // 90
```

### Enhanced For Loop (for-each)

Cleaner iteration when you don't need the index.

```java
for (int item : shoppingList) {
    System.out.println(item);
}
```

### Methods

```java
// Method with arguments and return value
public static int add(int a, int b) {
    return a + b;
}

// Calling the method
int result = add(3, 4); // 7
```

### Method Overloading (Static Polymorphism)

Multiple methods with the same name but different parameter types or counts. The compiler picks the correct one at compile time.

```java
public static int add(int a, int b) {
    return a + b;
}

public static double add(double a, double b) {
    return a + b;
}

// Usage
add(2, 3);       // calls int version
add(2.0, 3.5);   // calls double version
```

### String vs StringBuilder vs StringBuffer

**Analogy:** `String` is a fixed piece of paper — once written, you tear it up and write a new one for every change. `StringBuilder` / `StringBuffer` are flexible cloth you can keep adding to.

| Type            | Mutable | Thread-safe | Use case                              |
|-----------------|---------|-------------|---------------------------------------|
| `String`        | No      | Yes         | Fixed text, constants                 |
| `StringBuilder` | Yes     | No          | Single-threaded string building       |
| `StringBuffer`  | Yes     | Yes         | Multi-threaded string building        |

```java
// String — immutable
String fixed = "Hello";
String fixed2 = fixed + " World"; // creates a new String object

// StringBuilder — mutable, not thread-safe
StringBuilder mutable = new StringBuilder("Hello");
mutable.append(" World");
System.out.println(mutable.toString()); // Hello World

// StringBuffer — mutable, thread-safe
StringBuffer safe = new StringBuffer("Hello");
safe.append(" World");
```
