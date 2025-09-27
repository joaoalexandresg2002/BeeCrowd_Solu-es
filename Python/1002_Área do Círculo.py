# Lê um valor fornecido pelo usuário e o converte para um número decimal (float).
# Este valor representa o raio de um círculo.
raio = float(input())

# Calcula a área do círculo usando a fórmula: A = π * r²
# Aqui usamos π = 3.14159 (valor aproximado).
# O operador ** é exponenciação, então raio ** 2 significa raio ao quadrado.
# O :.4f formata o resultado com 4 casas decimais.
# A f-string (f"text {variavel}") permite misturar texto e valores na mesma string.
print(f"A={3.14159 * raio ** 2:.4f}")