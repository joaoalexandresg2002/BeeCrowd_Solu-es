# Lê dois números inteiros: hora inicial (h1) e hora final (h2)
h1, h2 = map(int, input().split())

# Calcula a diferença de horas entre início e fim do jogo
# O operador % 24 garante o ciclo de 24h (ex: 22 → 6 = 8h)
# O "or 24" cobre o caso em que a diferença é 0 (jogo durou 24h)
diferenca = (h2 - h1) % 24 or 24

# Exibe a duração total do jogo no formato solicitado
print(f"O JOGO DUROU {diferenca} HORA(S)")
