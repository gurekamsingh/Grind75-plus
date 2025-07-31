# Problem:
# Given a string s, find the length of the longest substring without repeating characters.

# A set is an unordered collection of unique elements.
# Think of it like a bag that:
# Can’t hold duplicates; Lets you check membership fast (O(1) time); Supports add/remove/lookups quickly

s = "abcabcdbb" 

def longestsubstring(s):
    seen = set()
    left = 0
    max_sum = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_sum = max(max_sum, right - left + 1)
    return max_sum

print(longestsubstring(s))  # Output: 4

# We can use I as left and j as right pointer to keep track of the current substring too.
# We can use a sliding window approach to solve this problem in O(n) time.
