# Lê todos os valores da entrada padrão e converte para inteiros
entrada = map(int, open(0).read().split())

# Cria um iterador a partir dos números lidos, permitindo percorrê-los com next()
e = iter(entrada)

# Loop infinito para processar os dados até que não haja mais valores
while True:
    try:
        # Pega os próximos 4 valores do iterador por vez: a, b, c e d
        a, b, c, d = [next(e) for _ in range(4)]

        # Variável que indica se os valores passam em todas as condições
        valida = False

        # Primeira condição: b deve ser maior que c e d deve ser maior que a
        if (b > c) and (d > a):
            # Soma de c e d, e soma de a e b (serão usadas para comparar)
            cmaisd = c + d
            amaisb = a + b

            # Segunda condição: a soma de c e d deve ser maior que a soma de a e b
            if cmaisd > amaisb:
                # Terceira condição: c e d devem ser positivos
                if (c > 0) and (d > 0):
                    # Quarta condição: a deve ser um número par
                    if a % 2 == 0:
                        valida = True  # Todas as condições foram atendidas

        # Se todas as condições forem verdadeiras, imprime "Valores aceitos"
        if valida:
            print("Valores aceitos")
        # Caso contrário, imprime "Valores nao aceitos"
        else:
            print("Valores nao aceitos")

    # Quando o iterador acabar (sem mais dados na entrada), o loop é interrompido
    except StopIteration:
        break
