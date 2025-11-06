# Problem - Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Input: s = "racecar", t = "carrace"
# Output: true


class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        counts = {}
        countt = {}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            countt[t[i]] = 1 + countt.get(t[i], 0)

        return counts == countt
    
s = "racecar"
t = "carrace"
print(Solution().isAnagram(s, t))  # Output: True    

# if we use -> for letter in s:
#     counts[letter] = 1 + counts.get(letter, 0)
# ok… that only handles string s.
# You completely lose the ability to iterate t in sync with the same index. You can’t index t from that loop directly. So you can’t do countt[t[i]] in that form.