"""
Question: 143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]
"""
from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        curr = slow.next
        prev = slow.next = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        first, second = head, prev
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            
"""
    Time-complexity = O(n)
    Space-complexity = O(1)

    Alternative solutions:
"""