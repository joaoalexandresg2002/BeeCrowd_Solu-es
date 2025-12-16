n = int(input())                           # Lê a quantidade de "Ho" que serão impressos

ho = ["Ho" if i != n-1 else "Ho!" for i in range(n)]
# Cria uma lista com "Ho" para cada posição
# Quando chegar no último índice (n-1), coloca "Ho!" com exclamação

print(*ho)                                  # Imprime todos os elementos separados por espaço
