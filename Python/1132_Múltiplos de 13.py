entrada = list(map(int, open(0).read().split()))  # Lê dois inteiros da entrada
x, y = sorted(entrada)                            # Ordena para garantir que x ≤ y

# Cria uma lista com números entre x e y (inclusive) que não são múltiplos de 13
soma = [i for i in range(x, y + 1) if i % 13 != 0]

print(sum(soma))  # Soma todos os valores filtrados e imprime o resultado
