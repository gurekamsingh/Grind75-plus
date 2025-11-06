# Problem: Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Input: nums = [1, 2, 3, 3]
# Output: true

class Solution:
    def hasdup(self, nums: list[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
    
nums = [245, 6557, 1, 646, 6, 5, 4, 3, 2, 1]
print(Solution().hasdup(nums))  # Output: True