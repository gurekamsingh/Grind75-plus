# Probelm: find the maximum sum of a subarray of size k.
# We can use a sliding window approach to solve this problem in O(n) time.

def maxsumsubarr(arr, k):
    windowsum = sum(arr[:k])
    max_sum = windowsum

    for i in range(k, len(arr)):
        windowsum += arr[i] - arr[i-k]
        max_sum = max(max_sum, windowsum)


    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3
print("Maximum sum of subarray of size k is:",maxsumsubarr(arr, k))  # Output: 9