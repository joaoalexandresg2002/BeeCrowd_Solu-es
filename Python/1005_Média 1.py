# Lê o primeiro número real (pode ter casas decimais)
a = float(input())
# Lê o segundo número real
b = float(input())

# Calcula a média ponderada dos dois valores
# O primeiro número (a) tem peso 3.5
# O segundo número (b) tem peso 7.5
# A soma dos pesos é 11
media = (a * 3.5 + b * 7.5) / 11

# Mostra o resultado formatado com 5 casas decimais
print(f"MEDIA = {media:.5f}")
