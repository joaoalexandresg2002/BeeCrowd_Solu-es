n = int(input())  # Lê um número inteiro que define o limite superior

# Loop de 1 até n (inclusive)
for i in range(1, n + 1):
    if i % 2 != 0:     # Verifica se o número é ímpar (resto da divisão por 2 ≠ 0)
        print(i)        # Imprime o número ímpar
