entrada = map(int, open(0).read().split()[1:])  # Lê todos os números da entrada, ignora o primeiro (que é a quantidade)

for valor in entrada:  # Percorre cada número informado
    # Calcula a soma dos divisores próprios (até metade do número, pois ninguém maior que isso é divisor)
    soma = sum(i for i in range(1, valor // 2 + 1) if valor % i == 0)
    
    # Verifica se o número é perfeito e imprime o resultado
    print(f"{valor} eh perfeito" if soma == valor else f"{valor} nao eh perfeito")
