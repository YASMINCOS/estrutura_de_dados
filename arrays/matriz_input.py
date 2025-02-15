linhas = 3
colunas = 3
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite um número para posição ({i},{j}): "))
        linha.append(valor)
    matriz.append(linha)

print("Matriz gerada:")
for linha in matriz:
    print(linha)
