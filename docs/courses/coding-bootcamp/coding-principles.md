---
tags:
  - coding
  - principles
  - best-practices
  - software-engineering
---

# Coding Principles

Reference notes on foundational software engineering principles — what they mean, why they matter, and how they appear in code.

---

## General Principles

### KISS — Keep It Simple, Stupid

Write the simplest code that correctly solves the problem. Avoid over-engineering, clever abstractions, or unnecessary complexity.

**Why it matters:** Complex code is harder to read, test, and debug. Future-you (and teammates) will thank you for clarity.

```java
// Over-engineered
public boolean isEvenOverEngineered(int n) {
    return Math.abs(n % 2) == 0 ? Boolean.TRUE : Boolean.FALSE;
}

// Simple — just do it
public boolean isEven(int n) {
    return n % 2 == 0;
}
```

---

### DRY — Don't Repeat Yourself

Every piece of knowledge or logic should have a single, authoritative representation. If you copy-paste code, refactor it into a reusable function or class.

**Why it matters:** Duplicated code means bugs get fixed in one place but not another.

```java
// Violates DRY — discount logic duplicated
double priceForMember = total * 0.9;
double priceForVip = total * 0.9;

// DRY — extract to a method
public double applyDiscount(double total, double rate) {
    return total * (1 - rate);
}

double memberPrice = applyDiscount(total, 0.10);
double vipPrice    = applyDiscount(total, 0.20);
```

---

### YAGNI — You Aren't Gonna Need It

Don't build features, abstractions, or flexibility until they are actually required.

**Why it matters:** Unused code adds complexity, increases maintenance burden, and may never be used.

```java
// YAGNI violation — building a plugin system nobody asked for
public interface PaymentProcessor { ... }
public class StripeAdapter implements PaymentProcessor { ... }
public class PayPalAdapter implements PaymentProcessor { ... }
// The product only accepts Stripe. PayPal isn't needed yet.

// YAGNI-compliant — just implement what's needed now
public void processPayment(double amount) {
    stripe.charge(amount);
}
```

---

### BDUF — Big Design Upfront

Design the entire system architecture before writing any code. This was the dominant approach in waterfall development.

**Modern view:** Generally considered an anti-pattern in Agile environments. Extensive upfront design delays delivery and often produces systems that don't match real requirements. Prefer iterative design with just enough upfront thinking.

**When it may apply:** Safety-critical systems (medical devices, aerospace) where design errors are catastrophic and expensive to fix.

---

### Occam's Razor

Among competing solutions, prefer the simplest one that fully addresses the problem. Don't introduce new entities, abstractions, or complexity without necessity.

**In code:** If two implementations solve the same problem equally well, choose the one with fewer moving parts.

---

### Law of Demeter (Principle of Least Knowledge)

A class should only communicate with its immediate collaborators — not reach through objects to talk to distant ones.

**Rule of thumb:** Call methods on objects you own, objects passed to you, or objects you created. Don't chain through multiple objects.

```java
// Violates LoD — reaching through customer to get city
String city = order.getCustomer().getAddress().getCity();

// Compliant — ask the order directly
String city = order.getCustomerCity(); // Order fetches this internally
```

---

### Avoid Premature Optimization

Don't optimize code for performance before you know there is a bottleneck. Measure first, then optimize the specific hotspot.

**Donald Knuth:** "Premature optimization is the root of all evil."

**Process:** Write correct, readable code → profile and measure → optimize only the proven bottleneck.

---

### Measure Twice, Cut Once

Carefully plan and verify requirements before making changes — especially destructive or hard-to-reverse ones.

**In code:** Think through data migrations, schema changes, and API contracts before implementing. Mistakes here are expensive.

---

### Principle of Least Astonishment

Code should behave in the way its users and fellow developers would reasonably expect. Surprising behavior is a design smell.

```java
// Astonishing — "add" that also sends an email? Unexpected side effect.
public void addUser(User user) {
    database.save(user);
    emailService.sendWelcome(user); // caller didn't expect this
}

// Less astonishing — separate concerns clearly
public void registerUser(User user) {
    database.save(user);
    emailService.sendWelcome(user); // "register" implies full onboarding
}
```

---

## SOLID Principles

SOLID is an acronym for five object-oriented design principles that make software easier to maintain, extend, and test.

### S — Single Responsibility Principle

A class should have only one reason to change. One class, one job.

```java
// Violates SRP — this class handles data, formatting, AND persistence
public class Report {
    public String generateContent() { ... }
    public String formatAsHtml() { ... }
    public void saveToDatabase() { ... }
}

// SRP-compliant — each class has one responsibility
public class Report {
    public String generateContent() { ... }
}

public class ReportFormatter {
    public String toHtml(Report report) { ... }
}

public class ReportRepository {
    public void save(Report report) { ... }
}
```

---

### O — Open/Closed Principle

A class should be open for extension but closed for modification. Add new behavior by extending, not by editing existing code.

**Example:** Use inheritance or interfaces to add new payment types without touching existing payment logic.

---

### L — Liskov Substitution Principle

Subclasses must be substitutable for their base class without altering the correctness of the program.

**Example:** If `Bird` has a `fly()` method, a `Penguin` subclass that throws an exception on `fly()` violates LSP. A `Penguin` should not extend a `Bird` with flight behavior.

---

### I — Interface Segregation Principle

Don't force clients to depend on interfaces they don't use. Prefer many small, specific interfaces over one large general one.

```java
// Violates ISP — a Robot is forced to implement eat()
public interface Worker {
    void work();
    void eat();
}

// ISP-compliant — split into focused interfaces
public interface Workable { void work(); }
public interface Feedable  { void eat();  }

public class HumanWorker implements Workable, Feedable { ... }
public class RobotWorker  implements Workable          { ... }
```

---

### D — Dependency Inversion Principle

High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.

```java
// Violates DIP — high-level service depends directly on a concrete class
public class OrderService {
    private MySQLDatabase db = new MySQLDatabase(); // concrete dependency

    public void placeOrder(Order order) {
        db.save(order);
    }
}

// DIP-compliant — depend on an abstraction (interface)
public interface Database {
    void save(Order order);
}

public class MySQLDatabase implements Database {
    public void save(Order order) { /* MySQL logic */ }
}

public class OrderService {
    private final Database db;

    public OrderService(Database db) { // injected — not created here
        this.db = db;
    }

    public void placeOrder(Order order) {
        db.save(order);
    }
}
// Now you can swap MySQLDatabase for PostgresDatabase or a mock in tests
// without touching OrderService at all.
```

---

## Quick Reference

| Principle                    | One-liner                                               |
|------------------------------|---------------------------------------------------------|
| KISS                         | Simple code is better code                              |
| DRY                          | One source of truth; no copy-paste logic                |
| YAGNI                        | Build it when you need it, not before                   |
| BDUF                         | Design upfront (mostly an anti-pattern in Agile)        |
| Occam's Razor                | Simplest solution that works                            |
| Law of Demeter               | Only talk to your immediate neighbors                   |
| Avoid Premature Optimization | Measure first, then optimize                            |
| Measure Twice, Cut Once      | Plan carefully before making hard-to-reverse changes    |
| Least Astonishment           | Code should behave as expected                          |
| SRP                          | One class, one reason to change                         |
| OCP                          | Extend, don't modify                                    |
| LSP                          | Subclasses must honor the base class contract           |
| ISP                          | Small focused interfaces, not one bloated interface     |
| DIP                          | Depend on abstractions, not concrete implementations    |
