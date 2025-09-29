# Lê três números decimais (float), separados por espaço
# O input() recebe a linha, split(" ") separa em lista, map(float, ...) converte cada valor
a, b, c = map(float, input().split(" "))

# Calcula e imprime a área de diferentes figuras geométricas usando f-strings
# f-strings permitem colocar expressões dentro das chaves {} e :.3f formata com 3 casas decimais
print(f"TRIANGULO: {a * c / 2:.3f}")        # Área do triângulo: base=a, altura=c -> (a*c)/2
print(f"CIRCULO: {c ** 2 * 3.14159:.3f}")   # Área do círculo: raio=c -> π*c² (π≈3.14159)
print(f"TRAPEZIO: {(a + b) * c / 2:.3f}")   # Área do trapézio: bases=a,b, altura=c -> ((a+b)*c)/2
print(f"QUADRADO: {b * b:.3f}")             # Área do quadrado: lado=b -> b²
print(f"RETANGULO: {a * b:.3f}")            # Área do retângulo: lados=a,b -> a*b