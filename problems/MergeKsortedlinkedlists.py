from typing import List
# Problem: Merge K Sorted Linked Lists
# You are given an array of k linked lists, each linked list is sorted in ascending order. 
# Merge all the linked lists into one sorted linked list and return it.

#brute force approach:
# Convert each linked list to an array, merge the arrays, and convert the merged array back to a linked list.
# This approach has a time complexity of O(n log k) where n is the total number of nodes across all lists and k is the number of linked lists.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: ListNode):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:  
            mergedlist = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedlist.append(self.mergelist(l1, l2)) # using mergelist helper function to merge two lists in sorted manner
            lists = mergedlist
        return lists[0] # Final merged list

    def mergelist(self, l1, l2):
        dummy = ListNode()
        tail = dummy  # tail is the pointer to the next node to be added in the merged list

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1  # If l1's value is smaller, add it to the merged list.
                l1 = l1.next    # move to the next node in l1
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:  # If there are remaining nodes in l1, add them to the merged list
            tail.next = l1
        if l2:  # If there are remaining nodes in l2, add them to the merged list
            tail.next = l2
        return dummy.next
    
#Time Complexity: O(N log k) where N is the total number of nodes across all lists and k is the number of linked lists. This is because we are merging k lists, and each merge operation takes O(N) time.
#Space Complexity: O(1) as we are not using any extra space for merging, just pointers.
