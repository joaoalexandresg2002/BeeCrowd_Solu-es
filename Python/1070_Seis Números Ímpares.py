n = int(input())

# Garante que começa no próximo ímpar (ou no próprio, se já for ímpar)
inicio = n if n % 2 else n + 1

# Usa range com passo 2 para pular direto entre ímpares
for i in range(inicio, inicio + 12, 2):
    print(i)
