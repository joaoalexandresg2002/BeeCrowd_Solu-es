entrada = open(0).read().split()[1:]  # Lê toda a entrada e ignora o primeiro valor (quantidade de casos)
e = iter(entrada)                     # Cria um iterador para percorrer os valores em pares (quantidade e tipo)

soma = 0  # Total de cobaias
# Dicionário para armazenar a contagem de cada tipo de animal
experimentos = {'C': 0, 'R': 0, 'S': 0}

# Percorre os dados em pares (quantidade, tipo)
for n, q in zip(e, e):
    n = int(n)
    soma += n                # Soma o total de cobaias
    experimentos[q] += n     # Soma a quantidade por tipo (C, R, S)

# Exibe o total geral e por categoria
print(f"Total: {soma} cobaias")
print(f"Total de coelhos: {experimentos['C']}")
print(f"Total de ratos: {experimentos['R']}")
print(f"Total de sapos: {experimentos['S']}")

# Exibe os percentuais de cada tipo, com duas casas decimais
print(f"Percentual de coelhos: {(experimentos['C'] / soma) * 100:.2f} %")
print(f"Percentual de ratos: {(experimentos['R'] / soma) * 100:.2f} %")
print(f"Percentual de sapos: {(experimentos['S'] / soma) * 100:.2f} %")
