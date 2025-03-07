def quicksort(lista):
    if len(lista) <= 1:
        return lista  # Lista já está ordenada
    else:
        pivo = lista[0]  # Escolhe o primeiro elemento como pivô
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

# Teste
numeros = [5, 3, 8, 4, 2]
print(quicksort(numeros))  # Saída: [2, 3, 4, 5, 8]
