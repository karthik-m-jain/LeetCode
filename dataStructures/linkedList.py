class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        if index == 0:
            self.insertAtBegin(data)
        else:
            current = self.head
            position = 0
            while(current.next != None and position + 1 == index):
                position += 1
                current = current.next
            
            if(current == None):
                print("Index not present")
            else:
                new_node.next = current.next
                current.next = new_node

    def updateNode(self, val, index):
        current = self.head
        position = 0
        while(position != index):
            position += 1
            current = current.next
        
        current.data = val

    def printLL(self):
        current = self.head
        while(current != None):
            print(current.data, "->", end =" ")
            current = current.next

ld = LinkedList()
ld.insertAtBegin(2)
ld.insertAtIndex(3,0)
ld.insertAtIndex(4,1)
ld.updateNode(6,0)
ld.printLL()

            
