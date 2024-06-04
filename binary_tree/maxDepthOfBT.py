"""
Question: 104. Maximum Depth of Binary Tree

    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    Example 1:

    Input: root = [3,9,20,null,null,15,7]
    Output: 3

    Example 2:

    Input: root = [1,null,2]
    Output: 2
"""
from typing import Optional
from typing import Deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Solution 1 -> Recursive DFS
        """
        if root is None:
            return 0
        
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        return 1 + max(l, r)
        """

        #Solution 2 -> Iterative DFS
        """
        stack = [[root, 1]]
        result = 0

        while stack:
            node, depth = stack.pop()

            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result
        """

        #Solution 3 -> Recursive BFS
        if not root:
            return 0

        queue = Deque([root])
        level = 0
        
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return level

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(sol.maxDepth(root))

"""
    Time-complexity = O(n)
    Space-complexity = O(n) - Height of the tree - In this, it is the worst-csae

    Alternative solutions:
    1. Recursive DFS (Implemented)
    2. Iterative BFS (No-change in complexities)
    3. Recursive BFS (No-change in complexities)
"""