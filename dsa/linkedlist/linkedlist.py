class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def delete(self, data):
        temp = self.head
        while temp and temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()
    
    def reverse(self):
        prev, cur = None, self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev

list1 = LinkedList()
list1.insert_start(5)
list1.insert_end(10)
list1.insert_end(20)
list1.display()
list1.delete(10)
list1.display()
list1.insert_start(5)
list1.head = list1.reverse()
list1.display()