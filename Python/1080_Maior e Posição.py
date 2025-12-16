nums = []  # Lista para armazenar os 100 números

# Lê 100 números inteiros e adiciona na lista
for i in range(100):
    n = int(input())
    nums.append(n)

# Exibe o maior número da lista
print(max(nums))

# Exibe a posição (1-based) do maior número
print(nums.index(max(nums)) + 1)
