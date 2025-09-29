# Lê uma linha de entrada digitada
# separa pelos espaços (split) e converte cada valor para inteiro (map(int, ...)).
# Depois transforma em uma lista para poder manipular facilmente.
n = list(map(int, input().split()))

# Usa a função max() para encontrar o maior valor dentro da lista 'n'
# e imprime no formato solicitado pelo problema.
print(f"{max(n)} eh o maior")