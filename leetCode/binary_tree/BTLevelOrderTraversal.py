"""
Question: 102. Binary Tree Level Order Traversal

    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

    Example 1:

    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Example 2:

    Input: root = [1]
    Output: [[1]]

    Example 3:

    Input: root = []
    Output: []
"""
from typing import Deque, Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        queue = Deque()
        queue.append(root)
        result = []

        while queue:
            temp = []

            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(temp)

        return result
            
"""
    Time-complexity = O(n)
    Space-complexity = O(n) -> For a tree at the left node (which has highest number of nodes) can have max n/2 nodes and our queue can contain that many nodes

    Alternative solutions:
"""

