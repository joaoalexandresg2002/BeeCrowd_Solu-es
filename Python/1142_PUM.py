n = int(input())          # Lê o número de linhas a serem impressas
c = 1                     # Contador inicial

for i in range(n):        # Loop principal para cada linha
    for j in range(3):    # Imprime três números seguidos
        print(c, end=" ") # Mostra o número na mesma linha
        c += 1            # Incrementa o contador
    c += 1                # Pula o número que seria o quarto (omitido)
    print("PUM")          # Imprime "PUM" no final da linha
