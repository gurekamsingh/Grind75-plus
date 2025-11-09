# You are given a list of events from Kafka. Each entry has a user_id and status like:
events = [
  {"user":"u1", "status":"success"},
  {"user":"u2", "status":"fail"},
  {"user":"u1", "status":"success"},
  {"user":"u3", "status":"fail"}
]
# Return a dictionary with count of success and fail grouped by status.

def eventstatus(events):
    result = {}
    for e in events:
        s = e["status"]
        result[s] = result.get(s, 0) + 1
    return result

print(eventstatus(events))