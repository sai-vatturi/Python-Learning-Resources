class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insertAtBegin(self, data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
            return
        else:
            new_Node.next = self.head
            self.head = new_Node
    
    def insertAtEnd(self, data):
        new_Node = Node(data)
        if  self.head is None:
            self.head = new_Node
            self.tail = new_Node
            return
        else:
            tail.next = new_Node
            tail = new_Node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()
        
l = LinkedList()
l.insertAtBegin(1)
l.insertAtBegin(2)
l.insertAtBegin(3)

l.display()