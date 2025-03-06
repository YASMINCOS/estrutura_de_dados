class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # Insere no topo

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove do topo
        return "A pilha está vazia!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Último elemento
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop()) 
print(stack.peek())  
