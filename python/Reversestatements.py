# Given a sentence, reverse the order of words but don’t reverse characters inside words.

# Example:
s = "I love devops" 
# → "devops love I"

def rev(s):
    words = s.split()
    res = words[::-1]
    return " ".join(res)

print(rev(s))

# for output: spoved love I

def rev(s):
    words = s.split()
    res = words[::-1]

    res[0] = res[0][::-1]

    return " ".join(res)

print(rev(s))