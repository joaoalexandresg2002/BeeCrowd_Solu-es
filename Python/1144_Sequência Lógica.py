n = int(input())                 # Lê um número inteiro 'n' da entrada

for i in range(1, n + 1):        # Percorre de 1 até 'n'
    print(i, i ** 2, i ** 3)     # Primeira linha: número, quadrado e cubo
    print(i, i ** 2 + 1, i ** 3 + 1)  # Segunda linha: cada valor somado de 1
