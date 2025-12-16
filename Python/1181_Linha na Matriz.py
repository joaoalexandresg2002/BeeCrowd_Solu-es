linha = int(input())              # Lê o número da linha que será usada
op = input().strip().upper()      # Lê a operação (S ou M), limpa e coloca em maiúsculas

# Lê a matriz 12x12 preenchendo com valores float
matriz = [[float(input()) for _ in range(12)] for _ in range(12)]

soma = sum(matriz[linha])         # Soma todos os valores da linha escolhida

# Se a operação for S, mostra a soma; se for M, mostra a média
print(f"{soma:.1f}" if op == "S" else f"{soma / 12:.1f}")
