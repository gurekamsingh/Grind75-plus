# problem: Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
# Example usage:       
# l1 = [2 -> 4 -> 3] (represents the number 342)
# l2 = [5 -> 6 -> 4] (represents the number 465)
# Output: [7 -> 0 -> 8] (represents the number 807)

# timecompexity = O(max(m, n)) where m and n are the lengths of the two linked lists.
# spacecompexity = O(max(m, n)) for the output linked list.

# brute force approach:
# Convert the linked lists to integers, add them, and convert the result back to a linked list.     
# This approach has a time complexity of O(n) but requires extra space for the integer conversion and may not handle very large numbers well.