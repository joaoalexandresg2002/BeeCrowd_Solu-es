e = map(int, open(0).read().split())  # Lê todos os valores da entrada e converte para int

for i, n in enumerate(e):  # Percorre cada número junto com seu índice
    # Se o valor for menor ou igual a 0, imprime 1; caso contrário imprime o próprio valor
    print(f"X[{i}] = {1}" if n <= 0 else f"X[{i}] = {n}")
