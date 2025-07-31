# Given an array of integers, count the frequency of each integer in the array.
def countfreq(arr):
    mp = {}

    for num in arr:
        mp[num] = mp.get[num, 0] + 1
print(mp)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 2, 6, 5, 4, 4, 4, 3, 7]
countfreq(arr)