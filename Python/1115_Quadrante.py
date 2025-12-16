entrada = map(int, open(0).read().split())  # Lê todos os inteiros da entrada
e = iter(entrada)                           # Cria um iterador para percorrer os valores

# Lê pares (x, y) até encontrar um zero
for x, y in zip(e, e):
    if x == 0 or y == 0:                    # Se algum for zero, o programa termina
        break

    # Determina o quadrante do ponto (x, y)
    if x > 0 and y > 0:
        ponto = "primeiro"
    elif x < 0 and y > 0:
        ponto = "segundo"
    elif x < 0 and y < 0:
        ponto = "terceiro"
    else:  # x > 0 and y < 0
        ponto = "quarto"

    print(ponto)                            # Exibe o quadrante correspondente
