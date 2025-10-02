# Lê as coordenadas do primeiro ponto (x1, y1) separadas por espaço
# Converte cada valor para float (número decimal)
x1, y1 = map(float, input().split())
# Lê as coordenadas do segundo ponto (x2, y2) separadas por espaço
x2, y2 = map(float, input().split())

# Calcula a distância entre os dois pontos usando a fórmula:
# distância = √((x2 - x1)² + (y2 - y1)²)
# Em Python, ** é operador de potência. Aqui usamos ** (1/2) para calcular a raiz quadrada.
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

# Imprime a distância com 4 casas decimais
print(f"{distancia:.4f}")
