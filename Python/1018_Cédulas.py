# Lê um número inteiro da entrada e armazena em 'n'
# Esse número representa o valor em reais que será decomposto em cédulas.
n = int(input())
# Lista com os valores das cédulas disponíveis no sistema monetário brasileiro
cedulas = [100, 50, 20, 10, 5, 2, 1]

# Imprime o valor original, como o problema pede
print(n)

# Percorre cada valor de cédula na lista
for cedula in cedulas:
    # Calcula quantas notas daquela cédula cabem no valor atual
    print(f"{n // cedula} nota(s) de R$ {cedula},00")
    # Atualiza o valor de 'n' para o resto da divisão (o que sobrou após retirar as notas daquela cédula)
    n %= cedula
