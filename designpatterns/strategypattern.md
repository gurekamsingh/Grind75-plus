# 🧩 Strategy Pattern (Design Pattern Notes)

## What is the Strategy Pattern?

The Strategy Pattern is a behavioral design pattern that enables selecting an algorithm or behavior at runtime. It does this by defining a common interface for a group of interchangeable strategies and delegating the behavior to the selected one.

Rather than hardcoding a specific behavior, the Strategy Pattern allows you to **plug in different strategies** dynamically.

It’s most useful when:
- You have multiple ways to perform a task
- You want to swap them in and out without changing the client logic
- You want to reduce the complexity of if-else or switch-case logic

---

## Key Concepts

- **Strategy**: An interface or abstract class defining a common behavior
- **Concrete Strategies**: Different classes implementing the strategy behavior
- **Context**: The class that uses the strategy object to execute behavior

The client doesn’t know (or care) which strategy is used — it just calls the common interface.

---

## Real-World Examples

- Navigation apps offering different routes (Driving, Walking, Cycling)
- Payment systems supporting Credit Card, PayPal, Crypto
- Sorting algorithms selected at runtime (QuickSort, MergeSort, BubbleSort)
- Text editors applying different formatting rules (UpperCase, LowerCase, TitleCase)

---

## Advantages of Strategy Pattern

- **Open/Closed Principle**: Easily add new strategies without changing existing code
- **Removes Complex Conditionals**: Replaces large if-else blocks with cleaner polymorphic behavior
- **Runtime Flexibility**: Change the behavior of a class without modifying its structure
- **Better Separation of Concerns**: Each strategy handles its own logic

---

## 🔍 Common Interview Questions & Answers

### ❓ Why is the Strategy pattern better than if-else statements?

**Answer**:  
If-else blocks become messy and hard to maintain as the number of cases grows. Strategy Pattern replaces them with clean, modular classes that encapsulate specific behaviors. This makes the code more maintainable, testable, and open to extension without modifying the core logic.

---

### ❓ When would you use Strategy vs. Factory?

**Answer**:  
Use **Strategy** when you want to choose *how* something is done — multiple behaviors that can be swapped (e.g., payment processing methods).  
Use **Factory** when you want to decide *what* object to create — especially when object creation is complex or involves inheritance.

In short:
- Strategy = interchangeable behaviors
- Factory = object creation logic

---

### ❓ How would you add a new strategy (e.g., `CryptoPayment`)?

**Answer**:  
You simply create a new class that implements the same interface as other strategies (like CreditCard or PayPal). The Context class does not need any changes. This aligns with the Open/Closed Principle: your system is open for extension, but closed for modification.

---

### ❓ How can you inject strategy dynamically (e.g., via user input)?

**Answer**:  
You can determine the strategy at runtime based on user input, configuration files, command-line args, or external data. Once selected, you inject the strategy into the context. This allows behavior to be fully dynamic without touching core business logic.

---

## Summary

The Strategy Pattern is ideal for situations where multiple interchangeable behaviors exist. It leads to cleaner, more modular code, avoids hardcoding logic with conditionals, and offers runtime flexibility.

It’s a go-to pattern for real-world systems that require adaptability — and a favorite in interviews for testing your design instincts.
