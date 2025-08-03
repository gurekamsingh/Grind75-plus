# 👀 Observer Design Pattern (with Python Example)

The **Observer Pattern** is a behavioral design pattern where a **subject** (or publisher) maintains a list of **observers** (or subscribers) and notifies them automatically of any state changes.

This is great for **event-driven systems**, **notification triggers**, or **decoupled updates**.

---

## 📦 Components in This Code

| Class               | Role                    | Description                                      |
|--------------------|-------------------------|--------------------------------------------------|
| `Observer`         | Abstract Observer       | Defines the `update()` method to be implemented |
| `EmailService`     | Concrete Observer       | Sends email when notified                       |
| `InventoryService` | Concrete Observer       | Updates stock info when notified                |
| `OrderPublisher`   | Subject / Publisher     | Manages observers and notifies them             |

---

## 🧠 How It Works

1. We define an abstract `Observer` class with an `update(message)` method.
2. `EmailService` and `InventoryService` inherit from `Observer` and implement `update`.
3. `OrderPublisher` has:
   - A list of observers (subscribers)
   - A `subscribe()` method to add observers
   - A `notify()` method that loops through observers and calls `update(message)`
4. When an order is placed, `notify("Order placed")` triggers both services.

---

## 📤 Example Output

```python
Sending email: Order placed for item #123
Updating inventory: Order placed for item #123
```
## ❓ Common Questions

### 1. What's the difference between Observer and Pub/Sub?

- **Observer**: Observers are tightly registered to the Subject directly.
- **Pub/Sub**: A middle layer (like a message broker) separates publishers from subscribers.

---

### 2. When would you use Observer over Strategy or Factory?

- Use **Observer** when you want to trigger side effects in **many components** based on one **state change**.
- **Strategy** is for selecting *how* something should behave.
- **Factory** is for deciding *which object* to create.

---

### 3. How would you implement Observer Pattern in Python?

- You’d define a `Subject` class with methods like `attach(observer)`, `detach(observer)`, and `notify()`.
- Observers would implement an `update()` method.

---

## ✅ Why Use It?

- **Decouples objects**: Subject doesn’t need to know details about observers.
- **Flexible**: Observers can come and go without changing the Subject’s logic.
- Great for **event-driven systems**, **notification systems**, and **reactive programming**.
