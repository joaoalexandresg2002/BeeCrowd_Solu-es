x, y = map(int, input().split())  # Lê dois números inteiros: 'x' (colunas) e 'y' (último número da sequência)
c = 1                             # Inicia o contador com 1
matriz = []                       # Lista que guardará as linhas da matriz

while c < y:                      # Continua enquanto 'c' for menor que 'y'
    m = []                        # Cria uma nova linha
    for i in range(x):            # Adiciona 'x' números por linha
        m.append(c)               # Adiciona o número atual à linha
        c += 1                    # Incrementa o contador
    matriz.append(m)              # Adiciona a linha completa à matriz

for valor in matriz:              # Percorre as linhas da matriz
    print(*valor)                 # Imprime cada linha separando os números por espaço
