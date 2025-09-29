# Lê um valor inteiro da entrada e armazena em 'x'.
# Esse valor representa a distância percorrida (em km).
x = int(input())
# Lê um valor decimal (float) da entrada e armazena em 'y'.
# Esse valor representa o total de combustível gasto (em litros).
y = float(input())

# Calcula o consumo médio dividindo a distância pelo combustível.
# O resultado é formatado com 3 casas decimais e acompanhado da unidade "km/l".
print(f"{x / y:.3f} km/l")
