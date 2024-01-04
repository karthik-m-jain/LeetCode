"""
Question:
    Implement queue from scratch and its functions add(item), remove(), peek(), isEmpty()
"""
class Queue():
    def __init__(self):
        self.__index = []

    def __len__(self):
        return len(self.__index)
    
    def add(self, item):
        self.__index.append(item)

    def remove(self):
        if len(self.__index) == 0:
            raise Exception ("remove() called on empty queue.")
        return self.__index.pop(0)

    def peek(self):
        if len(self.__index) == 0:
            raise Exception ("peek() called on empty queue")
        return self.__index[0]
    
    def isEmpty(self):
        return len(self.__index) == 0

solution = Queue()

solution.add("Karthik")
print(solution.peek())
print(solution.remove())
print(solution.isEmpty())

"""
    Time-complexity = 
    1. push = O(1)
    2. pop = O(1)
    3. peek = O(1)
    4. isEmpty = O(1)

    Space-complexity = O(n)
"""