def bubble_sort(lista):
    n = len(lista)  # Pegamos o tamanho da lista
    for i in range(n):  # Percorremos a lista 'n' vezes
        for j in range(0, n - i - 1):  # Percorremos até o último elemento não ordenado
            if lista[j] > lista[j + 1]:  # Se o elemento atual for maior que o próximo, trocamos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Swap (troca de posição)

# Exemplo de uso
numeros = [5, 3, 8, 4, 2]
bubble_sort(numeros)
print(numeros)  # Saída: [2, 3, 4, 5, 8]
