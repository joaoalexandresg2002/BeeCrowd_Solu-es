coluna = int(input())      # Lê o número da coluna desejada
op = input().strip().upper()   # Lê a operação (S ou M) e deixa maiúscula

# Lê a matriz 12x12 de valores float
matriz = [[float(input()) for _ in range(12)] for _ in range(12)]

# Soma apenas os elementos da coluna escolhida
soma = sum(
    matriz[i][j]
    for i in range(12)
    for j in range(12)
    if j == coluna        # Garante que só soma a coluna desejada
)

# Se a operação for S, imprime a soma; senão imprime a média
print(f"{soma:.1f}" if op == "S" else f"{soma / 12:.1f}")
