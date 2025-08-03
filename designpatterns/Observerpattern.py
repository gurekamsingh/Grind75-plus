# Imagine a YouTube Channel (Subject) and many Subscribers (Observers).
# Whenever the channel uploads a new video, all the subscribers get notified.

# That’s the Observer Pattern.



class observer:
    def update(self, message):
        pass

class Emailnotification(observer):
    def update(self,message):
        print(f"Email Notification: {message}")

class InventoryService(observer):
    def update(self, message):
        print(f"Inventory Service Notification: {message}")

class Orderpublisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def notify(self, message):
        for subscribers in self.subscribers:
            subscribers.update(message)

order = Orderpublisher()
order.subscribe(Emailnotification())
order.subscribe(InventoryService())

order.notify("Order placed for item #123")

# Real-World Use:
# Imagine you're building an e-commerce platform. When a new order is placed, you want to notify both the customer via email and update the inventory service.
# This Observer pattern implementation allows you to easily add or remove notification methods without changing the core order processing logic.