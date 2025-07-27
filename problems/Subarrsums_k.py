# Problem desc: Find number of Subrray in a array nums that  sums to k.

# Brute  force would be nested loops i->j will result in O(n²)

# Optimized solution is in Hashmaps using prefix sum
# We use a running sum (prefix sum) to track the total as we move through the array.
# A dictionary stores how often each sum has appeared so far.
# If the difference between the current sum and k has been seen before, it means there's a subarray that sums to k.



nums = [2,2,-1,4,-4,2,6,4]
k = 4

def subarr(nums, k):
    count = 0
    currentsum = 0
    prefix_sum_count={0:1}

    for num in nums:
        currentsum += num

        if currentsum - k in prefix_sum_count:
        # Increase the count of how many times I have seen the subarr that sums to k current sum(i) - previous sum(j) = k  
             count += prefix_sum_count[currentsum - k]

        # Increment the count of how many times we've seen this prefix sum so far.
        prefix_sum_count[currentsum] = prefix_sum_count.get(currentsum, 0) + 1

    return count

print(subarr(nums,k))