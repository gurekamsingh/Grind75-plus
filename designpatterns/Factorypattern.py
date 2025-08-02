# Real-World Use:
# Imagine you're building a notification system — sometimes it's an Email, sometimes it's SMS, or Slack

class Notification:
    def send(self, message): pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationFactory:
    @staticmethod
    def create_notification(channel):
        if channel == "email":
            return EmailNotification()
        elif channel == "sms":
            return SMSNotification()
        else:
            raise ValueError("Invalid channel")

# Usage
notifier = NotificationFactory.create_notification("email")
notifier.send("Your order was shipped.")
