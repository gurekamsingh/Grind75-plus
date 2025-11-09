# Given a string representing log content, return the top 1 most frequent word.


def mostfrequentword(log):
    result = {}
    words = log.split()
    for w in words:
        result[w] = result.get(w, 0) + 1
    
    return max(result, key=result.get)

log = "error error timeout connection error timeout"
print(mostfrequentword(log))