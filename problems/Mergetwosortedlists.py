# Problem: Merge Two Sorted Lists
# You are given the heads of two sorted linked lists. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.    
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify numss1 in-place instead.
        """
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:   # Compare the last elements of both arrays
                # Place the larger element at the end of nums1
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        while n > 0:    # If there are remaining elements in nums2, copy them over
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1

            
# Time complexity: O(m + n) where m and n are the lengths of the two lists.
# space complexity: O(1) as we are modifying nums1 in-place without using extra space.         
# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3       
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]