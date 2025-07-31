# Given an array of integers, count the frequency of each integer in the array.

def countfreq(arr):
    mp = {}

    for num in arr:
        mp[num] = mp.get(num, 0) + 1
    print(mp)

arr = [11, 2, 13, 4, 5, 6, 7, 1, 2, 6, 5, 14, 14, 14, 13, 7]
countfreq(arr)


# mp is a dictionary that stores frequencies. You can imagine it like this: {number: count}
# mp.get(num, 0) tries to fetch the current count of num from the dictionary.
# If num is not in mp, it returns 0 (default).
# + 1 increases the count by 1.

# So mp[num] = mp.get(num, 0) + 1 either:
# Adds a new key with value 1, if the number hasn’t been seen yet
# Updates the existing key by adding 1, if it’s already been seen