matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][2])  # Acessa o elemento da linha 1, coluna 2 → 6
for linha in matriz:
    for item in linha:
        print(item, end=" ")
    print()
