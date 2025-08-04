# Problem: Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
# A string is called a palindrome when it reads the same backward as forward. 
# A substring is a contiguous sequence of characters within the string.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start  = 0
        end = 0

        for i in range(len(s)):
            # odd length
            l,r = i, i  # two pointers, in left  both l and r point to the same index i
            while l >= 0 and r < len(s) and s[l] == s[r]: # expand around center
                if (r - l + 1) > end:
                    start = l
                    end = r - l + 1
                l -= 1
                r += 1
                
            # even length   
            l,r = i, i + 1   # in right, left pointer l points to index i and in right pointer r points to index i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > end:
                    start = l
                    end = r - l + 1
                l -= 1
                r += 1

        return s[start: start + end]
    
# Time Complexity: O(n^2) where n is the length of the string. This is due to the nested while loops that can potentially expand to the entire length of the string for each character.
# Space Complexity: O(1) as we are using only a constant amount of extra space.
# Example usage:
s = "babad"
print(Solution().longestPalindrome(s))  # Output: "bab" or "aba"