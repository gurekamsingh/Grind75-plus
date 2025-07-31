# Problem:
# Given a string s, find the length of the longest substring without repeating characters.
s = "abcabcdbb" 

def longestsubstring(s):
    seen = set()
    left = 0
    max_sum = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[right])
            left += 1
        seen.add(s[right])
        max_sum = max(max_sum, right - left + 1)
    return max_sum

print(longestsubstring(s))  # Output: 3
