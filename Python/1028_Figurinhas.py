from math import gcd  # Importa a função gcd (máximo divisor comum)

# Lê todos os números inteiros da entrada padrão
entrada = map(int, open(0).read().split())
e = iter(entrada)

n = next(e)  # Lê o primeiro valor, que indica quantos pares serão processados

# Loop que executa n vezes
for i in range(n):
    a, b = next(e), next(e)  # Lê dois números inteiros
    print(gcd(a, b))         # Imprime o MDC (máximo divisor comum) entre eles
