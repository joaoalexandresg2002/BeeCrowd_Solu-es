op = input().strip().upper()   # Lê a operação (S ou M) e converte para maiúscula

matriz = [[float(input()) for _ in range(12)] for _ in range(12)]  
# Lê a matriz 12x12 preenchendo linha por linha

soma = sum(
    matriz[i][j]              # Pega o valor da posição (i, j)
    for i in range(7, 12)         # Percorre as 6 primeiras linhas (parte superior da matriz)
    for j in range(12 - i, i)  # Seleciona apenas os elementos da área inferior da matriz
)

# Se a operação for S, mostra a soma; senão mostra a média
# OBS: a região possui 30 elementos, por isso divide por 30
print(f"{soma:.1f}" if op == "S" else f"{soma / 30:.1f}")
