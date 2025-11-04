# Lê quatro inteiros: hora e minuto de início (h1, m1) e hora e minuto de fim (h2, m2)
h1, m1, h2, m2 = map(int, input().split())

# Converte o horário de início e fim para minutos totais desde 0h
inicio = h1 * 60 + m1
fim = h2 * 60 + m2

# Calcula a diferença em minutos, considerando ciclo de 24h
diferenca = (fim - inicio) % (24 * 60)

# Converte a diferença em horas e minutos
horas = diferenca // 60
minutos = diferenca % 60

# Caso especial: se diferença for 0, o jogo durou 24h
if horas == 0 and minutos == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    # Exibe a duração total em horas e minutos
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
