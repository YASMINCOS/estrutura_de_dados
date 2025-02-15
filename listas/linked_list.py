class Node:
    def __init__(self, data):
        self.data = data  # Armazena o valor do nó
        self.next = None  # Ponteiro para o próximo nó

class LinkedList:
    def __init__(self):
        self.head = None  # Inicialmente, a lista está vazia

    def insert(self, data):
        new_node = Node(data)  # Criamos um novo nó
        new_node.next = self.head  # O novo nó aponta para o antigo primeiro nó
        self.head = new_node  # O novo nó se torna a nova cabeça da lista

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Criando e testando a lista ligada
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
print("Lista ligada após inserções:")
ll.display()