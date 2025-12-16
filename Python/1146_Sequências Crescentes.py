while True:                            # Loop infinito até encontrar a condição de parada
    n = int(input())                   # Lê um número inteiro
    if n == 0:                         # Se o número for 0, o programa termina
        break
    nums = [i for i in range(1, n+1)]  # Cria uma lista com os números de 1 até n
    print(*nums)                       # Imprime todos os números da lista separados por espaço
