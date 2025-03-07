def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        menor = i  # Supondo que o primeiro elemento seja o menor
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:  # Se encontrar um número menor, atualiza o índice
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]  # Faz a troca

# Teste
numeros = [5, 3, 8, 4, 2]
selection_sort(numeros)
print(numeros)  # Saída: [2, 3, 4, 5, 8]
