# ☕ Decorator Pattern – Coffee Example

## ✅ What is the Decorator Pattern?

The **Decorator Pattern** allows you to **add new functionality to objects dynamically** — without modifying the original class.

Instead of creating a huge number of subclasses to cover all combinations of features, you **wrap** the base object in decorators that each add one feature.

---

## 🔧 Real-World Analogy

Imagine you're ordering a coffee:
- You start with a basic coffee.
- You can add **milk**, **sugar**, or an **espresso shot**.
- Each add-on increases the cost.
- You don’t need a new `MilkSugarEspressoCoffee` class — just layer decorators.

---

## 🛠️ Python Example: Coffee Decorators

```python
class Coffee:
    def cost(self):
        return 5  # base coffee cost

class CoffeeDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 2  # adds milk cost

class EspressoDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 5  # adds espresso shot cost

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 1  # adds sugar cost

# Ordering process
order = Coffee()
print(order.cost())  # Output: 5

# Add sugar, then milk, then espresso
order = EspressoDecorator(MilkDecorator(SugarDecorator(order)))
print(f"Order for coffee with one espresso shot with milk and sugar is ${order.cost()}")
# Output: 5 (base) + 1 (sugar) + 2 (milk) + 5 (espresso) = 13
```
## ❓ Interview Questions & Answers

### 1. What’s the difference between Decorator and Subclassing?

- **Decorator** adds behavior to objects at runtime without changing their code.
- **Subclassing** adds behavior at compile-time but can lead to a deep inheritance hierarchy.
- Decorator promotes composition over inheritance and keeps classes modular.

---

### 2. When should you use Decorator over Strategy or Factory?

- Use **Decorator** when you want to add responsibilities dynamically (e.g., logging, auth).
- Use **Strategy** when you need to swap behaviors/algorithms (e.g., sorting, payment methods).
- Use **Factory** when you want to control which object gets created without exposing the instantiation logic.

---

### 3. Can Decorators be stacked or nested?

Yes. You can layer decorators to build up behavior step-by-step.

Example:  
`Coffee()` → `SugarDecorator()` → `MilkDecorator()` → `EspressoDecorator()`

---

### 4. What are the benefits of the Decorator Pattern?

- Adheres to the **Open/Closed Principle**: extend behavior without modifying existing code.
- Avoids class explosion due to feature combinations.
- Keeps individual features modular and reusable.

---

### 5. Is Decorator similar to Middleware?

Yes. Middleware (like in Express.js or Django) works like a decorator that wraps requests/responses with additional behavior like logging, validation, or caching.

---
