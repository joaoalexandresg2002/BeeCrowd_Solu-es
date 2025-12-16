# Lista de ímpares de 3 a 39
b = list(range(3, 40, 2))

# Lista dobrando: 1, 2, 4, 8...
a = [1]
for _ in range(len(b) - 1):
    a.append(a[-1] * 2)

# Soma dos pares correspondentes
soma = sum(x + y for x, y in zip(a, b))

print(f"{soma / 87500:.2f}")
