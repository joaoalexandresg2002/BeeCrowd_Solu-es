# Lê todos os números inteiros da entrada, ignorando o primeiro (quantidade de casos)
entrada = map(int, open(0).read().split()[1:])
e = iter(entrada)  # Cria um iterador para percorrer os valores em pares

# Loop que lê os números de dois em dois (x e y)
for valor in zip(e, e):
    x, y = sorted(valor)  # Ordena para garantir que x < y
    # Soma todos os números ímpares estritamente entre x e y
    soma = sum(i for i in range(x + 1, y) if i % 2 != 0)
    print(soma)  # Exibe o resultado da soma
