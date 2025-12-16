op = input().strip().upper()   # Lê a operação (S ou M) e converte para maiúscula

matriz = [[float(input()) for _ in range(12)] for _ in range(12)]  
# Lê a matriz 12x12 preenchendo linha por linha

soma = sum(
    matriz[i][j]          # Pega o valor da posição (i, j)
    for i in range(12)    # Percorre as linhas
    for j in range(12)    # Percorre as colunas
    if j > i              # Condição: pega somente a parte acima da diagonal principal
)

# Se a operação for S, mostra a soma; caso contrário, mostra a média (dividido por 66)
print(f"{soma:.1f}" if op == "S" else f"{soma / 66:.1f}")
