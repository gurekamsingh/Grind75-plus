# You are processing messages from a queue.
# You get a list of customer order events. Each event has a customer_id.
# Count how many unique customers placed orders.
events = [
 {"customer":"c1"},
 {"customer":"c2"},
 {"customer":"c1"},
 {"customer":"c3"},
 {"customer":"c2"},
]

def uniquecustomers(events):
    result = set()
    for e in events:
        result.add(e["customer"])
    return len(result)

print(uniquecustomers(events))