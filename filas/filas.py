class Fila:
    def __init__(self):
        self.itens = []
    
    def enfileirar(self, item):
        self.itens.append(item)
    
    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None
    
    def esta_vazia(self):
        return len(self.itens) == 0
    
    def tamanho(self):
        return len(self.itens)
        

fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

print (f"tamanho da fila {fila.tamanho()}")

print(fila.desenfileirar())
print(fila.desenfileirar())

print (f"tamanho da fila {fila.tamanho()}")
