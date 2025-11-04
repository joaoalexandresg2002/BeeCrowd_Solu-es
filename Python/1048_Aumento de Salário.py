# Lê o salário atual do funcionário
salario = float(input())

# Inicializa a variável do percentual de aumento
aumento = 0

# Define o percentual de aumento com base na faixa salarial
if salario > 2000:
    aumento = 0.04       # 4% para salários acima de 2000
elif salario > 1200:
    aumento = 0.07       # 7% para salários entre 1200 e 2000
elif salario > 800:
    aumento = 0.10       # 10% para salários entre 800 e 1200
elif salario > 400:
    aumento = 0.12       # 12% para salários entre 400 e 800
else:
    aumento = 0.15       # 15% para salários até 400

# Calcula e exibe o novo salário com aumento
print(f"Novo salario: {salario + salario * aumento:.2f}")

# Exibe o valor do reajuste ganho
print(f"Reajuste ganho: {salario * aumento:.2f}")

# Exibe o percentual de aumento aplicado
print(f"Em percentual: {aumento * 100:.0f} %")
