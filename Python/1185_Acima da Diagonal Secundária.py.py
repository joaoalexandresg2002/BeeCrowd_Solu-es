op = input().strip().upper()   # Lê a operação (S ou M) e converte para maiúscula

matriz = [[float(input()) for _ in range(12)] for _ in range(12)]  
# Lê a matriz 12x12 preenchendo linha por linha

soma = sum(
    matriz[i][j]              # Pega o valor da posição (i, j)
    for i in range(11)        # Percorre as linhas de 0 até 10
    for j in range(11 - i)    # Percorre as colunas limitando para ficar acima da diagonal secundária
)

# Se a operação for S, mostra a soma; caso contrário, mostra a média (dividida por 66)
print(f"{soma:.1f}" if op == "S" else f"{soma / 66:.1f}")
