e = list(map(int, open(0).read().split()[1:]))  # Lê todos os números da entrada, ignora o primeiro e converte para lista de inteiros

print(f"Menor valor: {min(e)}")                 # Imprime o menor valor da lista
print(f"Posicao: {e.index(min(e))}")            # Imprime o índice onde o menor valor aparece
