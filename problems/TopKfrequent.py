# Problem:
# Given an integer array arr and an integer k, return the k most frequent elements.


# Instead of using a heap (which gives us O(n log k)), we can:
# Count frequencies → O(n)
# Group numbers by frequency using buckets → O(n)
# Traverse buckets in reverse to grab the top k → O(n)

from collections import Counter

def topkfreq(arr, k):

# Counter: quickly counts how many times each number appears in nums.  This builds a dictionary with num as key and freq as value
    freqmp = Counter(arr)
    n = len(arr)
    buckets = [[] for i in range(n + 1)]

    for num, freq in freqmp.items():
       buckets[freq].append(num)


    result=[]

    for i in range(n, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result 
            

# Example usage:
arr = [1, 1, 1, 2, 2, 3, 3, 3]
k = 2
print(topkfreq(arr, k))  # Output: [1, 3]        

# Time and Space Complexity: O(n)

# So basically, we are counting the fequency of each number through counter and then we use bucket sort 
# In a way that we create a dictionary where the key is the frequency and the value is a list of numbers that have that frequency.
# then we traverse the buckets in reverse order to get the top k frequent elements. 
# such that we get the most frequent elements first.
