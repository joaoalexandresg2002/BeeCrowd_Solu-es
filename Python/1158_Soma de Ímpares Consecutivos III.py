entrada = map(int, open(0).read().split()[1:])   # Lê todos os inteiros da entrada, ignorando o primeiro
e = iter(entrada)                                # Cria um iterador para consumir os valores

for a, b in zip(e, e):                           # Lê pares de valores (a, b)
    inicio = a if a % 2 != 0 else a + 1          # Garante que 'inicio' seja o primeiro número ímpar ≥ a
    print(sum(inicio + 2*i for i in range(b)))   # Soma os 'b' números ímpares consecutivos e imprime
