entrada = map(int, open(0).read().split()[1:])  # Lê todos os inteiros (ignorando o primeiro número, que indica a quantidade de casos)
e = iter(entrada)                               # Cria um iterador para percorrer os valores

# Lê pares (a, b) para realizar divisões
for a, b in zip(e, e):
    try:
        print(f"{a / b:.1f}")                   # Exibe o resultado da divisão com uma casa decimal
    except ZeroDivisionError:                   # Captura divisão por zero
        print("divisao impossivel")             # Mensagem de erro para divisão inválida
