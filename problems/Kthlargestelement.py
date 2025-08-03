# Problem:
# Find the kth largest element in an unsorted array.
# Note: It’s not the kth distinct, just the kth in sorted order.

import heapq 
class Solution:
     def findKthLargest(self, nums: list[int], k: int):
# Converting nums from index 0 to k into a min-heap, Last leaf node is n/2 +1 and left child is 2*i + 1 and right child is 2*i + 2

        heap  = nums[:k]
        heapq.heapify(heap) # heapify converts list into a min-heap such that smallest element is at heap[0]

        for num in nums[k:]:
            if num > heap[0]: # If the current number is larger than the smallest in the heap, replace it
                heapq.heappush(heap, num) # push the new number onto the heap
                heapq.heappop(heap) # pop the smallest element to maintain size k
        return heap[0] # Element at index 0 will always be the kth largest element

nums = [2,3,1,5,4]
k = 2    
solution = Solution()
print(solution.findKthLargest(nums, k))  # Output: 4