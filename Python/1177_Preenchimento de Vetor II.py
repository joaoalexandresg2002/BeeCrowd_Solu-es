n = int(input())              # Lê um número inteiro que define o tamanho da lista
nums = list(range(n))         # Cria uma lista com valores de 0 até n-1

for i in range(1000):         # Loop que imprime 1000 posições
    print(f"N[{i}] = {nums[i % len(nums)]}")  
    # Usa i % len(nums) para repetir os valores da lista ciclicamente
