# Lê o primeiro número real (com casas decimais)
a = float(input())
# Lê o segundo número real
b = float(input())
# Lê o terceiro número real
c = float(input())

# Calcula a média ponderada dos três valores
# O primeiro número (a) tem peso 2
# O segundo número (b) tem peso 3
# O terceiro número (c) tem peso 5
# A soma dos pesos é 10
media = (a * 2 + b * 3 + c * 5) / 10

# Mostra o resultado formatado com 1 casa decimal
print(f"MEDIA = {media:.1f}")
