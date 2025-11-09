# You have log entries where each line is "timestamp,status_code".
# Find how many requests failed (status code >= 400).
logs = [
 "2025-05-10T12:01Z,200",
 "2025-05-10T12:01Z,500",
 "2025-05-10T12:02Z,404",
 "2025-05-10T12:03Z,200"
]

def failedrequests(logs):
    count = 0
    for l in logs:
        status = int(l.split(",")[1])
        if status >= 400:
            count += 1
    return count

print(failedrequests(logs))