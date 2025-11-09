# We have a list of events and each event has a region. Return a dictionary showing how many events happened per region.
events = [
 {"region":"us-east"},
 {"region":"us-east"},
 {"region":"ca-central"},
 {"region":"us-west"},
 {"region":"us-east"}
]

def allevents(events):
    result = {}
    for e in events:
        region = e["region"]
        result[region] = result.get(region, 0) + 1
    return result

print(allevents(events))