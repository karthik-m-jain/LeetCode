"""
Question:
    Implement stack from scratch and its functions pop(), push(), peek(), isEmpty()
"""

class Stack:
    def __init__(self):
        self.__index = []

    def __len__(self):
        return len(self.__index)
    
    def push(self, item):
        self.__index.insert(0, item)

    def pop(self):
        if len(self) == 0:
            raise Exception("pop() called on empty stack.")
        return self.__index.pop(0)
    
    def peek(self):
        if len(self) == 0:
            raise Exception("peek() called on empty stack. ")
        return self.__index[0]
    
    def isEmpty(self):
        return len(self) == 0

solution = Stack()

solution.push(1)
print(solution.peek())
print(solution.pop())
print(solution.isEmpty())

"""
    Time-complexity = 
    1. push = O(1)
    2. pop = O(1)
    3. peek = O(1)
    4. isEmpty = O(1)

    Space-complexity = O(n)
"""