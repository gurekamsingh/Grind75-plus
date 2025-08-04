# Problem: K Closest Points to Origin
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x^2 + y^2)).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).   
import heapq
class Solution:
    def kClosest(self, points: int, k: int):
        minheap = []

        for x, y in points:
            dist = x**2 + y**2
            minheap.append([dist, x, y])
        heapq.heapify(minheap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minheap)
            res.append([x, y])
            k -= 1
        return res
# Example usage:
points = [[1,3],[-2,2],[2,-2], [5,8],[0,1]]
k = 3
print(Solution().kClosest(points, k)) # Output: [[-2,2],[2,-2],[0,1]] (the order may vary)

# Time Complexity: O(n log n) where n is the number of points. This is due to the heap operations.
# Space Complexity: O(n) for storing the heap.
# This approach uses a min-heap to efficiently retrieve the k closest points to the origin based on their Euclidean distance.

# brute force approach:
# Calculate the distance for each point and sort them based on this distance.
# This approach has a time complexity of O(n log n) due to the sorting step, which is less efficient than using a heap for large datasets.