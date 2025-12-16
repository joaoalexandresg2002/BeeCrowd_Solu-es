from math import isqrt  # isqrt retorna a raiz quadrada inteira (mais rápido que sqrt)

e = map(int, open(0).read().split()[1:])  # Lê os números da entrada e ignora o primeiro (quantidade)

for n in e:  # Percorre cada número da entrada
    primo = True  # Assume que o número é primo até provar o contrário
    
    # Testa divisores de 2 até a raiz quadrada de n
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:  # Se houver divisor exato
            primo = False  # Não é primo
            break  # Interrompe o laço para otimizar

    # Imprime dependendo se é primo ou não
    print(f"{n} eh primo" if primo else f"{n} nao eh primo")
