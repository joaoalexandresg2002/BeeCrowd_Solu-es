d = iter(map(int, open(0).read().split()))  # Cria um iterador com os números inteiros da entrada
pessoas = 0                                 # Contador de pessoas (quantidade de valores válidos)
soma = 0                                    # Acumulador da soma dos valores

while True:                                 # Loop infinito até encontrar um número negativo
    n = next(d)                             # Lê o próximo número da entrada
    if n < 0:                               # Se o número for negativo, encerra o loop
        break
    pessoas += 1                            # Incrementa o número de pessoas
    soma += n                               # Soma o valor à soma total

print(f"{soma / pessoas:.2f}")              # Exibe a média dos valores com 2 casas decimais
