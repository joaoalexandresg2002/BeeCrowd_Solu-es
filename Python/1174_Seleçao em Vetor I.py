for i in range(100):            # Loop que percorre 100 posições
    n = float(input())          # Lê um número real
    if n <= 10:                 # Só imprime valores menores ou iguais a 10
        print(f"A[{i}] = {n:.1f}")  # Imprime com 1 casa decimal
