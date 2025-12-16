entrada = map(float, open(0).read().split())
e = iter(entrada)

while True:
    soma = 0
    c = 0
    while c < 2:
        num = next(e)                             # Lê a próxima nota
        if 0 <= num <= 10:                        # Verifica se a nota é válida
            soma += num                           # Soma a nota
            c += 1                                # Conta a nota válida
        else:
            print("nota invalida")  
    print(f"media = {soma / 2:.2f}")
    sair = 0
    while sair not in [1, 2]:
        sair = next(e)
        print("novo calculo (1-sim 2-nao)")
    if sair == 2:
        break