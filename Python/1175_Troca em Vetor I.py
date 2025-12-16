vetor = [0] * 20                      # Cria uma lista com 20 posições inicializadas em 0

for i in range(20):                   # Lê 20 valores do usuário
    vetor[i] = int(input())           # Armazena cada valor na posição correspondente

for i, valor in enumerate(reversed(vetor)):  # Percorre a lista ao contrário com índice
    print(f"N[{i}] = {valor}")        # Imprime no formato solicitado
