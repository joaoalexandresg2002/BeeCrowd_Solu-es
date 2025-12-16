e = iter(map(int, open(0).read().split()[1:]))  # Lê todos os números (exceto o primeiro) e cria um iterador

for a, b in zip(e, e):  # Pega os valores em pares (a, b) do iterador
    print(a + b)        # Soma cada par e imprime o resultado
