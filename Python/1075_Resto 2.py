n = int(input())  # Lê um número inteiro de entrada

# Percorre todos os números de 1 até 10000 (inclusive)
for i in range(1, 10000 + 1):
    if i % n == 2:     # Verifica se o resto da divisão de i por n é igual a 2
        print(i)        # Se for, imprime o número
