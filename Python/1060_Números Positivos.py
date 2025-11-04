# Lê todos os valores de entrada como números decimais (float)
entrada = map(float, open(0).read().split())
e = iter(entrada)  # Cria um iterador para percorrer os valores

contador = 0  # Contador de números positivos

# Loop que percorre os 6 valores da entrada
for i in range(6):
    if next(e) > 0:  # Verifica se o valor atual é positivo
        contador += 1  # Incrementa o contador se for positivo

# Exibe quantos valores positivos foram informados
print(f"{contador} valores positivos")
