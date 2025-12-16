entrada = map(int, open(0).read().split())
e = iter(entrada)
for valor in zip(e, e):
    x, y = valor
    if x == y:
        break
    print("Crescente" if x < y else "Decrescente")