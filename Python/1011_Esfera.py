# Lê o valor do raio da esfera (pode ter casas decimais)
raio = float(input())

# Calcula o volume da esfera usando a fórmula:
# V = (4/3) * π * raio^3
# Em Python, ** representa a potência (raio ** 3 = raio ao cubo)
volume = (4/3) * 3.14159 * raio ** 3

# Mostra o volume calculado, formatado com 3 casas decimais
print(f"VOLUME = {volume:.3f}")
