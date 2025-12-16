x, y = map(int, open(0).read().split())

x, y = sorted((x, y))

soma = sum(i for i in range(x + 1, y) if i % 2 != 0)

print(soma)