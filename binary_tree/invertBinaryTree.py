"""
Question: 226. Invert Binary Tree

    Given the root of a binary tree, invert the tree, and return its root.

    Example 1:

    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    
    Example 2:

    Input: root = [2,1,3]
    Output: [2,3,1]
    
    Example 3:

    Input: root = []
    Output: []
"""

import sys

from typing import Optional
from dataStructures.binaryTree import TreeTraversal

# Definition for a binary tree TreeNode.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        temp = TreeNode()

        self.invertTree(root.left)
        self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp

        return root
    
solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

printTree = TreeTraversal()
printTree.inOrder(solution.invertTree(root))

"""
    Time-complexity = O(n)
    Space-complexity = O(1)

    Alternative solutions:
        1. 
"""
    
