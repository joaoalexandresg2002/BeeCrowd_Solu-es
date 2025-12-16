while True:
    n = int(input())                            # Lê um número inteiro
    if n == 0:                                   # Se for 0, encerra o loop
        break
    
    inicio = n if n % 2 == 0 else n + 1          # Garante que 'inicio' seja o próximo número par ≥ n
    print(sum(inicio + 2*i for i in range(5)))   # Soma 5 números pares consecutivos e imprime
