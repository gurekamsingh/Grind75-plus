# Problem:
# Given an integer array nums and an integer target, return the indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

#brute force approach:
# Iterate through each pair of numbers and check if they add up to the target.
# This approach has a time complexity of O(n^2) and is not efficient for large arrays. 

class Solution:
    def twoSum(self, nums: int, target: int):
        seenmap = {} # key is num and value is index; [key:value]

        for i, num in enumerate(nums):          # enumerate function starts from 0 and add the elements one by one 
            secondnum = target - num 
            if secondnum in seenmap:
                return [seenmap[secondnum], i] 
            seenmap[num] = i                    # if not found, add the number and its index to the map 

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))  # Output: [0, 1] (because nums[0] + nums[1] == 9)

# Time Complexity: O(n) where n is the number of elements in nums
# Space Complexity: O(n) for the seenmap storage
# This approach uses a hash map to store the indices of the numbers, allowing for quick lookups to find the complement needed to reach the target sum.
# It ensures that we only traverse the list once, making it efficient for large inputs.