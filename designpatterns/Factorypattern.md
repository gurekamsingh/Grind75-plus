# 🏭 Factory Pattern

## What is the Factory Pattern?

The **Factory Pattern** is a creational design pattern that provides a way to **create objects without specifying the exact class** of the object that will be created.

Instead of instantiating classes directly using `new` or constructors, the Factory delegates object creation to a separate method (the "factory").

Strategy:
**I already have the barista. I’ll tell them to make my drink using this method.**

Factory:
**I go to the counter, ask for a drink by type (‘latte’, ‘espresso’), and they figure out which barista/machine to use and hand it to me.**

### 💡 Real-World Analogy

Think of a **notification system**:
- You may need to send notifications via Email, SMS, or Push.
- The Factory takes in a type (`"email"`, `"sms"`), and returns the correct object (`EmailSender`, `SMSSender`) without the client needing to know the class details.

---

## ✅ Why Use It?

- Encapsulates object creation logic
- Makes the system easier to extend (e.g., add new types)
- Follows the **Open/Closed Principle** — open for extension, closed for modification

---

## 🔁 Factory Pattern vs Strategy Pattern

| Pattern   | Focus                                | Client Knows Strategy? | Typical Use Case                        |
|-----------|----------------------------------------|------------------------|-----------------------------------------|
| Strategy  | Choosing *how* something is done       | Yes                    | Dynamic behavior switch (e.g., payment) |
| Factory   | Choosing *what object* to create       | No                     | Object creation (e.g., notification type) |

---

## 🧠 Common Interview Questions

---

### ❓ When would you prefer **Factory** over **Strategy**?

**Answer**:  
Use **Factory** when you want to **hide object creation logic** from the client and let the system decide *which concrete class to return*.

Use **Strategy** when you already have the object (or injected it) and want to vary its **behavior dynamically**.

> 🔑 Factory = create the right class  
> 🔑 Strategy = pick the right behavior

---

### ❓ What happens if new notification types (e.g., Slack) are added?

**Answer**:  
You just:
1. Create a new class like `SlackNotifier` that implements the `Notifier` interface.
2. Update the factory logic (or config) to return `SlackNotifier` for type `"slack"`.

This keeps the system **scalable and extendable** — no changes needed in client code or existing types.

---

### ❓ How can you make this dynamic (config-based or plugin-driven)?

**Answer**:  
Instead of hardcoding logic like:

```python
if type == "email": return EmailNotifier()
```