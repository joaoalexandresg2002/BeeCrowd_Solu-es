entrada = map(int, open(0).read().split()[1:])  # Lê todos os números da entrada e ignora o primeiro
for n in entrada:  # Percorre cada valor solicitado para calcular Fibonacci
    a, b = 0, 1  # Começa a sequência: F(0)=0, F(1)=1
    fibonacci = 0  # Variável que guardará o resultado final

    if n != 1:  # Caso geral: calcular Fibonacci para n > 1
        for i in range(2, n + 1):  # Loop da posição 2 até n
            a, b = b, a + b  # Atualiza os valores de Fibonacci
            fibonacci = b  # Guarda o valor atual (F(i))
        print(f"Fib({n}) = {fibonacci}")  # Exibe o resultado

    else:  # Caso especial: F(1)
        print("Fib(1) = 1")
