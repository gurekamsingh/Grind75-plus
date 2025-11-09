# You are given events in dict form:
events = [
 {"service":"billing","status":200,"latency":350},
 {"service":"auth","status":502,"latency":100},
 {"service":"search","status":404,"latency":180},
 {"service":"auth","status":200,"latency":50}
]
# Rules:
# if status >=500 → label = "server_error"
# elif status >=400 → "client_error"
# elif latency > 300 → "slow"
# else → "ok"

# Return how many per label (dictionary)

def labels(events):
    result = {}
    for e in events:
        s = e["status"]
        l = e["latency"]
        
        if s >= 500:
            key = "server_error"
        elif s > 400:
            key = "client_error"
        elif l > 300:
            key = "slow"
        else:
            key = "ok"

        
        result[key] = result.get(s, 0) + 1
    return result

print(labels(events))

