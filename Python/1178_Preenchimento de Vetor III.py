n = float(input())            # Lê um número real inicial

for i in range(100):          # Loop que irá repetir 100 vezes
    print(f"N[{i}] = {n:.4f}")  # Imprime o valor atual formatado com 4 casas decimais
    n /= 2                     # Divide o valor por 2 para a próxima iteração
