# Lê todos os números da entrada
dados = list(map(int, open(0).read().split()))
n, numeros = dados[0], dados[1:]  # Primeiro número é N, o restante são os valores

# Conta quantos estão dentro e fora do intervalo [10, 20]
soma_in = sum(10 <= num <= 20 for num in numeros)
soma_out = n - soma_in  # O restante são os que estão fora

# Exibe os resultados
print(f"{soma_in} in")
print(f"{soma_out} out")
