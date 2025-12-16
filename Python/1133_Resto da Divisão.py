entrada = list(map(int, open(0).read().split()))  # Lê dois inteiros da entrada

a, b = sorted(entrada)                            # Ordena para garantir que a < b

# Percorre os números entre a e b (excluindo os extremos)
for i in range(a + 1, b):
    # Imprime apenas os que deixam resto 2 ou 3 na divisão por 5
    if i % 5 in (2, 3):
        print(i)
