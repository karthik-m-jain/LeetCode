from typing import Optional

class Node:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class TreeTraversal:
    def inOrder(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return

        self.inOrder(root.left)
        print(root.val, end = ' ')
        self.inOrder(root.right)

    def preOrder(self, root = Optional[Node]) -> Optional[Node]:
        if root is None:
            return
        print(root.val, end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def postOrder(self, root = Optional[Node]) -> Optional[Node]:
        if root is None:
            return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val, end = " ")

solution = TreeTraversal()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

solution.inOrder(root)
print()
solution.preOrder(root)
print()
solution.postOrder(root)
print()
        
        
        


        