#problem: Group Anagrams
# Given an array of strings, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Regular dict we have to check if key is present in default no key check needed
        for s in strs:
            count = [0] * 26  # [0,0,0,0,...26 times]
            for c in s:
                count[ord(c) - ord('a')] += 1  # Assume first char is b ord['b'] - ord ['a'] is subtracting Ascii value of b from a which is 2
#  count[2] count becomes [0, 1, 0, 0, ..., 0]
            res[tuple(count)].append(s) # tupple cannot be modified once created we append the string(s) as value to tuple keys(count)
        return list(res.values())

# Basic logic keys are the count of what all char are present in a string and values are what the strings have that number of characters
# like bad count[1, 1, 0, 1, 0, ...] and dab also has the same count.
# 1b 1a 1d (key) : 'bad', 'dab'

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Time Complexity: O(n * k) where n is the number of strings and k is the maximum length of a string. This is because we iterate through each string and count the characters.
# Space Complexity: O(n * k) for storing the grouped anagrams in the result dictionary, where n is the number of strings and k is the maximum length of a string.