entrada = map(int, open(0).read().split())  # Lê todos os valores inteiros da entrada

contador = 0  # Inicializa o contador de números pares

# Percorre todos os valores lidos
for valor in entrada:
    if valor % 2 == 0:   # Verifica se o número é par (resto da divisão por 2 igual a 0)
        contador += 1    # Incrementa o contador se for par

# Exibe a quantidade total de valores pares
print(f"{contador} valores pares")
