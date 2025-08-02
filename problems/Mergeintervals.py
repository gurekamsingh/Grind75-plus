# Problem:
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals.
# Example:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

def merge(intervals):
# Each x is an interval like [1, 3],  key= tells sort() what to sort by
# lambda x: x[0] is an anonymous function that says “just use the first element of each interval as the sorting key”
    intervals.sort(key = lambda x: x[0])

    merged = []
    for interval in intervals:
# merged[-1][1] means second element of last interval in merged
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)

        else:
            merged[-1][1] = max(interval[1], merged[-1][1])
    return merged;


arr = [[1,5],[2,4]]
print(merge(arr))  # Output: [[1, 6], [8, 10], [15, 18]]


# Real-World Use:
# Imagine you're scheduling meetings in a calendar app. You need to merge overlapping time slots to avoid double bookings.
# This function helps you consolidate those time slots efficiently.

#  Time & Space:
# Time: O(n log n) for sorting

# Space: O(n) for output list