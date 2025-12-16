nums = list(map(int, open(0).read().split()))  # Lê todos os números inteiros da entrada e os armazena em uma lista

# Conta quantos números são pares (True = 1, False = 0, somando dá a contagem)
pares = sum(n % 2 == 0 for n in nums)

# A quantidade de ímpares é o total menos os pares
impares = len(nums) - pares

# Conta quantos números são positivos
positivos = sum(n > 0 for n in nums)

# Conta quantos números são negativos
negativos = sum(n < 0 for n in nums)

# Exibe as contagens formatadas conforme o enunciado
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
