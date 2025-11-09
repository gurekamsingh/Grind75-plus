# Given a list of log lines, return how many unique IPs accessed the service.
logs = [
"10.2.1.5 GET /login",
"10.2.1.5 GET /checkout",
"18.9.22.11 GET /home"
]


def Ips(logs):
    result = set()
    for l in logs:
        ip = l.split(" ")[0]
        result.add(ip)
    return len(result)


print(Ips(logs))


# Given two strings s and t, return True if t is an anagram of s, otherwise False.
# Example: 
s = "listen"
t = "silent" 

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    countS = {}
    countT = {}

    for i in range(len(s)):
        countS[i] = countS.get(s[i], 0) + 1
        countT[i] = countT.get(t[i], 0) + 1

    return countS == countT

print(isAnagram(s, t))