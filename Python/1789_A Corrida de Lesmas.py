e = iter(map(int, open(0).read().split()))   # Cria um iterador com todos os números da entrada

for n in e:                                   # Para cada caso, n indica quantos valores serão lidos
    nums = sorted(next(e) for _ in range(n))  # Lê n valores do iterador e ordena a lista
    m = nums[-1]                              # Pega o maior número (último após ordenar)
    
    # Imprime 1 se <10, 2 se entre 10 e 19, 3 se >= 20
    print(1 if m < 10 else 3 if m >= 20 else 2)
