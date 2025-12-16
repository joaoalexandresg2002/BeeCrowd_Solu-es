n = int(input())  # Lê um número inteiro que define o limite superior

# Percorre apenas os números pares de 2 até n (inclusive)
for i in range(2, n + 1, 2):
    # Exibe o número e o seu quadrado formatado no padrão pedido
    print(f"{i}^2 = {i * i}")
