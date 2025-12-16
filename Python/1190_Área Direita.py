op = input().strip().upper()   # Lê a operação (S ou M) e converte para maiúscula

matriz = [[float(input()) for _ in range(12)] for _ in range(12)]  
# Lê a matriz 12x12 preenchendo linha por linha

soma = sum(
    matriz[i][j]              # Pega o valor da posição (i, j)
    for j in range(11, 6, -1)         # Percorre as linhas 7 até 11 (parte inferior da matriz)
    for i in range(12 - j, j)  # Seleciona apenas os elementos da área à direita da matriz
)

# Se a operação for S, mostra a soma; senão mostra a média
# OBS: Essa região contém exatamente 30 elementos, por isso a divisão é por 30
print(f"{soma:.1f}" if op == "S" else f"{soma / 30:.1f}")
