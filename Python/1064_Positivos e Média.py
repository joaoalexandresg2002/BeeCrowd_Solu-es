entrada = map(float, open(0).read().split())  # Lê todos os valores de entrada como números decimais

contador = 0  # Conta quantos valores são positivos
soma = 0      # Soma dos valores positivos

# Percorre todos os valores da entrada
for valor in entrada:
    if valor > 0:          # Verifica se o número é positivo
        contador += 1       # Incrementa o contador
        soma += valor       # Adiciona o valor à soma

# Exibe a quantidade de valores positivos
print(f"{contador} valores positivos")
# Calcula e exibe a média dos valores positivos, com 1 casa decimal
print(f"{soma / contador:.1f}")
