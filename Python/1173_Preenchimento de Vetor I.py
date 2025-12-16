n = int(input())        # Lê o valor inicial

for i in range(10):     # Laço para gerar 10 posições
    print(f"N[{i}] = {n}")  # Imprime o valor atual
    n *= 2                  # Dobra o valor para a próxima posição
