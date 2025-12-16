n = int(input())             # Lê um número inteiro 'n'

for d in range(1, n + 1):    # Percorre todos os números de 1 até 'n'
    if n % d == 0:           # Verifica se 'd' é divisor de 'n'
        print(d)             # Se for divisor, imprime o valor
