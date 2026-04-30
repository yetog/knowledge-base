---
tags:
  - coding
  - java
  - course
---

# Java Advanced Topics

## Week 2 — Exception Handling, Date, and I/O

### Exception Handling

Exceptions are runtime errors that disrupt normal program flow. Java uses `try/catch/finally` to handle them gracefully.

**Checked exceptions** — must be handled at compile time (e.g., `IOException`, `SQLException`).
**Unchecked exceptions** — runtime errors not enforced by the compiler (e.g., `NullPointerException`, `ArrayIndexOutOfBoundsException`).

```java
// Basic try/catch/finally
try {
    int result = 10 / 0;
} catch (ArithmeticException e) {
    System.out.println("Error: " + e.getMessage());
} finally {
    System.out.println("Always runs — good for cleanup");
}

// Multiple catch blocks
try {
    String s = null;
    s.length(); // throws NullPointerException
} catch (NullPointerException e) {
    System.out.println("Null reference: " + e.getMessage());
} catch (Exception e) {
    System.out.println("General error: " + e.getMessage());
}
```

| Exception                          | Cause                                      |
|------------------------------------|--------------------------------------------|
| `NullPointerException`             | Calling a method on a null reference       |
| `ArrayIndexOutOfBoundsException`   | Accessing an array index that doesn't exist|
| `ArithmeticException`              | Illegal arithmetic (e.g., divide by zero)  |
| `ClassCastException`               | Invalid type cast                          |

### Date Class

Used to represent and manipulate dates and times.

```java
import java.util.Date;
import java.text.SimpleDateFormat;

Date now = new Date();
System.out.println(now); // current date/time

SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
String formatted = sdf.format(now);
System.out.println(formatted); // e.g., 2026-04-30
```

### I/O Streams

Java uses streams to read from and write to files.

```java
import java.io.*;

// Writing to a file
FileWriter fw = new FileWriter("output.txt");
BufferedWriter bw = new BufferedWriter(fw);
bw.write("Hello, file!");
bw.close();

// Reading from a file
FileReader fr = new FileReader("output.txt");
BufferedReader br = new BufferedReader(fr);
String line;
while ((line = br.readLine()) != null) {
    System.out.println(line);
}
br.close();
```

---

## Week 3 — Interfaces and Multithreading

### Interfaces

An interface defines a behavioral contract — what a class can do, not how it does it. A class can implement multiple interfaces (Java's way of achieving multiple inheritance for behavior).

```java
// Define an interface
public interface Drawable {
    void draw();
}

public interface Resizable {
    void resize(int factor);
}

// Implement multiple interfaces
public class Circle implements Drawable, Resizable {
    public void draw() {
        System.out.println("Drawing circle");
    }

    public void resize(int factor) {
        System.out.println("Resizing by factor " + factor);
    }
}
```

### Multithreading

Multithreading allows multiple tasks to run concurrently within the same program.

**Thread lifecycle:** New → Runnable → Running → Waiting/Blocked → Terminated

**Two ways to create a thread:**

```java
// Option 1: extend Thread
public class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running: " + getName());
    }
}
new MyThread().start();

// Option 2: implement Runnable (preferred)
Runnable task = () -> System.out.println("Runnable running");
new Thread(task).start();
```

### Thread Safety with `synchronized`

Without synchronization, multiple threads accessing shared data can cause race conditions.

```java
public class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}
```

---

## Week 4 — Java EE and Hibernate

### Java EE (Enterprise Edition)

Java EE is a platform for building large-scale, distributed, enterprise-grade applications. It adds a set of APIs and runtime services on top of Java SE.

Key components:

| Component | Purpose                                      |
|-----------|----------------------------------------------|
| Servlets  | Handle HTTP requests and responses           |
| JSPs      | Generate dynamic HTML on the server          |
| EJBs      | Managed server-side business logic components|
| JPA       | Java Persistence API — ORM standard          |

### Hibernate (ORM)

Hibernate is an ORM (Object-Relational Mapping) framework that maps Java classes to database tables, eliminating most raw SQL.

**Key annotations:**

```java
import jakarta.persistence.*;

@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "username")
    private String username;

    @Column(name = "email")
    private String email;

    // Getters and setters
}
```

**Core Hibernate objects:**

| Object           | Purpose                                          |
|------------------|--------------------------------------------------|
| `SessionFactory` | Created once at startup; heavyweight factory     |
| `Session`        | Lightweight; represents a single unit of work    |
| `Transaction`    | Wraps database operations in a transaction block |

```java
Session session = sessionFactory.openSession();
Transaction tx = session.beginTransaction();

User user = new User();
user.setUsername("isayah");
session.save(user);

tx.commit();
session.close();
```

---

## Week 5 — Maven and Spring Framework

### Maven

Maven is a build automation and dependency management tool. All dependencies and build config live in `pom.xml`.

```xml
<!-- pom.xml — add a dependency -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <version>3.2.0</version>
</dependency>
```

**Common Maven commands:**

| Command          | Action                                  |
|------------------|-----------------------------------------|
| `mvn clean`      | Delete generated files                  |
| `mvn compile`    | Compile source code                     |
| `mvn test`       | Run unit tests                          |
| `mvn package`    | Build a JAR/WAR                         |
| `mvn install`    | Install artifact to local repository    |

### Spring Framework

Spring uses Inversion of Control (IoC) / Dependency Injection (DI) to reduce boilerplate and decouple components. Instead of creating objects manually, Spring creates and injects them.

```java
// Mark a class as a Spring-managed component
@Service
public class UserService {
    public String greet() {
        return "Hello from UserService";
    }
}

// Inject it into another class
@Component
public class UserController {

    @Autowired
    private UserService userService;

    public void doSomething() {
        System.out.println(userService.greet());
    }
}
```

**Key annotations:**

| Annotation     | Purpose                                          |
|----------------|--------------------------------------------------|
| `@Component`   | Generic Spring-managed bean                      |
| `@Service`     | Business logic layer bean                        |
| `@Repository`  | Data access layer bean                           |
| `@Autowired`   | Inject a dependency automatically                |

---

## Week 6 — Spring Boot

### What is Spring Boot?

Spring Boot is an opinionated layer on top of Spring that follows "convention over configuration." It embeds a Tomcat server so you can run applications without deploying to an external server.

### Key Annotations

| Annotation              | Purpose                                               |
|-------------------------|-------------------------------------------------------|
| `@SpringBootApplication`| Enables auto-configuration, component scanning, config|
| `@RestController`       | Marks class as a REST API controller                  |
| `@GetMapping`           | Maps HTTP GET requests to a method                    |
| `@PostMapping`          | Maps HTTP POST requests to a method                   |
| `@PathVariable`         | Binds a URI segment to a method parameter             |
| `@RequestBody`          | Deserializes JSON request body into an object         |

### REST Controller Example

```java
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello World";
    }

    @GetMapping("/user/{id}")
    public String getUser(@PathVariable int id) {
        return "User ID: " + id;
    }
}
```

### Entry Point

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MyApp {
    public static void main(String[] args) {
        SpringApplication.run(MyApp.class, args);
    }
}
```

### application.properties

```properties
server.port=8080
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.datasource.password=secret
spring.jpa.hibernate.ddl-auto=update
```
