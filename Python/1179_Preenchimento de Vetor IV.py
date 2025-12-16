e = map(int, open(0).read().split())  # Lê todos os números da entrada como inteiros

par = []    # Lista para armazenar números pares temporariamente
impar = []  # Lista para armazenar números ímpares temporariamente

for v in e:  # Percorre cada valor lido
    (par if v % 2 == 0 else impar).append(v)  # Coloca o número na lista correspondente

    if len(par) == 5:  # Se já acumulei 5 pares
        print(*(f"par[{i}] = {x}" for i, x in enumerate(par)), sep="\n")  # Imprime os pares
        par.clear()  # Limpa a lista para receber novos valores

    if len(impar) == 5:  # Se já acumulei 5 ímpares
        print(*(f"impar[{i}] = {x}" for i, x in enumerate(impar)), sep="\n")  # Imprime os ímpares
        impar.clear()  # Limpa a lista

# Após terminar o loop, imprime o que sobrou nas listas (menos de 5 elementos)
print(*(f"impar[{i}] = {x}" for i, x in enumerate(impar)), sep="\n")  # Imprime ímpares restantes
print(*(f"par[{i}] = {x}" for i, x in enumerate(par)), sep="\n")      # Imprime pares restantes
