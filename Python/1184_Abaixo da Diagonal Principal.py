op = input().strip().upper()   # Lê a operação (S ou M) e converte para maiúscula

matriz = [[float(input()) for _ in range(12)] for _ in range(12)]  
# Lê a matriz 12x12 preenchendo linha por linha

soma = sum(
    matriz[i][j]          # Pega o valor da posição (i, j)
    for i in range(12)    # Percorre todas as linhas
    for j in range(12)    # Percorre todas as colunas
    if i > j              # Condição: pega somente a parte ABAIXO da diagonal principal
)

# Se a operação for S, mostra a soma; senão mostra a média (a região tem 66 elementos)
print(f"{soma:.1f}" if op == "S" else f"{soma / 66:.1f}")
