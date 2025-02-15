class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLikedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
          new_node.next = self.head
          self.head.prev = new_node
          self.head = new_node
    
    def display (self):
        current = self.head
        while current:
            print(current.data, end= '<->')
            current = current.next
        print("None")
        
lista = DoubleLikedList()
lista.insert(10)
lista.insert(20)
lista.insert(30)
print("lista após a inserçao")
lista.display()