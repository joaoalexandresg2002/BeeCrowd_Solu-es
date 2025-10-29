from math import sqrt

# Leitura dos coeficientes a, b e c
a, b, c = map(float, input().split())

# Calcula o discriminante (delta)
delta = b**2 - 4 * a * c

# Verifica se é possível calcular as raízes
if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    raiz_delta = sqrt(delta)
    denominador = 2 * a

    # Cálculo das raízes com clareza
    r1 = (-b + raiz_delta) / denominador
    r2 = (-b - raiz_delta) / denominador

    # Saída formatada com precisão de 5 casas decimais
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
