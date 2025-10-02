# Lê um número inteiro da entrada e armazena em 'x'
# Esse número representa a distância (em km) entre dois carros.
x = int(input())

# Calcula o tempo necessário para que um carro alcance o outro.
# A cada 1 km de distância, o carro demora 2 minutos.
# Então basta multiplicar a distância por 2.
print(x * 2, "minutos")
