"""
Question: 206. Reverse Linked List

    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Example 1:

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

    Example 2:

    Input: head = [1,2]
    Output: [2,1]

    Example 3:

    Input: head = []
    Output: []
    
    Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

    Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""
from typing import Optional
from dataStructures.linkedList import *

#TODO: LinkedList creation method

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # # Iterative
        # previous, current_node = None, head

        # while(current_node != None):
        #     temp = current_node.next
        #     current_node.next = previous
        #     previous = current_node
        #     current_node = temp
        
        # return previous
    
        # Recursive
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        
        head.next = None
        return newHead
        
"""
    Time-complexity = O(n)
    Space-complexity = O(1)

    Alternative solutions:
        1. Recursive method - T=O(n), S=O(n)  
"""