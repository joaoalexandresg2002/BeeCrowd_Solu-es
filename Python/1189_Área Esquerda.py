op = input().strip().upper()   # Lê a operação (S ou M) e converte para maiúscula

matriz = [[float(input()) for _ in range(12)] for _ in range(12)]  
# Lê a matriz 12x12 preenchendo linha por linha

soma = sum(
    matriz[i][j]              # Pega o valor da posição (i, j)
    for j in range(0, 5)      # Percorre as colunas de 0 a 4 (primeiras 5 colunas)
    for i in range(j+1, 11 - j)  # # Seleciona apenas os elementos da área à esquerda da matriz
)

# Se a operação for S, mostra a soma; senão mostra a média
# OBS: a região possui 30 elementos, por isso divide por 30
print(f"{soma:.1f}" if op == "S" else f"{soma / 30:.1f}")
