e = iter(open(0).read().split())  # Cria um iterador com todos os valores da entrada
n = int(next(e))                  # Lê o primeiro número (quantidade de casos)

# Loop que processa cada conjunto de três valores
for i in range(n):
    # Lê três números decimais e converte para float
    a, b, c = [float(next(e)) for i in range(3)]

    # Calcula a média ponderada com pesos 2, 3 e 5
    media = ((a * 2) + (b * 3) + (c * 5)) / 10

    # Exibe a média com uma casa decimal
    print(f"{media:.1f}")
