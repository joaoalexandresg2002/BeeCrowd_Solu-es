while True:
    n = int(input())
    if n == 0:
        break
    
    inicio = n if n % 2 == 0 else n + 1
    print(sum(inicio + 2*i for i in range(5)))