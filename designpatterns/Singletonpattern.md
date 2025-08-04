# 🔒 Design Pattern: Singleton

## 🧠 What is Singleton?

The **Singleton Pattern** ensures that a class has **only one instance** and provides a **global point of access** to that instance.

### 🧾 Real-World Analogy

Think of a **printer spooler** in an operating system. You don’t want multiple spoolers running at once, so the system ensures there's only **one**.

---

## ✅ When to Use

- Logging services
- Database connection pools
- Configuration managers
- Caching layers

---

## 🔧 Python Example

```python
class Singleton:
    _instance = None

    def __new__(cls): # cls is class to be instantiated
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls) #if instance doesn't exist then create one.
        return cls._instance

# Usage
a = Singleton()
b = Singleton()

print(a is b)  # Output: True (same instance)
```
## ❓ Interview Questions & Answers (Singleton Pattern)

---

### 1. Why use Singleton instead of a global variable?

- Singleton ensures **controlled access**, **lazy initialization**, and follows **object-oriented principles**.
- Global variables are accessible from anywhere, which can lead to unexpected overwrites and make the code harder to maintain or test.
- Singleton centralizes access while still keeping encapsulation and flexibility.

---

### 2. How do you implement Singleton in Python?

By overriding the `__new__()` method to ensure only one instance is created:

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
```
---

### 3. What are alternatives to Singleton?

- **Dependency Injection (DI)**: Instead of globally accessing the object, inject it where needed. Easier to test and mock.
- **Module-level singleton**: In Python, a module is a singleton by default. You can define the shared object in a module and import it wherever needed.

Use these when you want better testability, flexibility, or reduced global state.

---

### 4. Can Singleton break in multi-threaded environments?

Yes. If two threads simultaneously enter `__new__()` before `_instance` is set, both can create a new object, breaking the Singleton guarantee.

✅ Solution: Use a thread lock:

```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
```