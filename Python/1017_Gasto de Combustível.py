# Lê um valor inteiro e armazena em 'x'
# Esse valor representa o tempo gasto na viagem (em horas).
x = int(input())
# Lê outro valor inteiro e armazena em 'y'
# Esse valor representa a velocidade média durante a viagem (em km/h).
y = int(input())

# Calcula a quantidade de combustível necessária para a viagem.
# Fórmula: distância = tempo * velocidade
# consumo = distância / consumo_médio
# Como o carro faz 12 km/l, dividimos a distância por 12.
# O resultado é formatado com 3 casas decimais.
print(f"{x / 12 * y:.3f}")
