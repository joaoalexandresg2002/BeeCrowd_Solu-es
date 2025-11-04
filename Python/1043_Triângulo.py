# Lê toda a entrada padrão
# Converte todos os valores lidos para ponto flutuante (float)
entrada = map(float, open(0).read().split())

# Cria um iterador a partir da sequência 'entrada'
# Assim, podemos avançar pelos elementos conforme eles são consumidos
e = iter(entrada)

# Agrupa os números de 3 em 3 usando zip(e, e, e)
# Cada grupo (a, b, c) representa três lados possíveis de um triângulo
for a, b, c in zip(e, e, e):

    # Verifica a condição de existência de um triângulo
    # Regra: a soma de dois lados precisa ser maior que o terceiro, para os três casos
    if a + b > c and a + c > b and b + c > a:
        # Se for um triângulo válido, calcula o perímetro (soma dos lados)
        resposta = a + b + c
        # Exibe o resultado com uma casa decimal
        print(f"Perimetro = {resposta:.1f}")
    else:
        # Caso não forme um triângulo, calcula a "área do trapézio"
        # usando a fórmula: área = ((a + b) * c) / 2
        resposta = ((a + b) * c) / 2
        # Exibe o resultado formatado com uma casa decimal
        print(f"Area = {resposta:.1f}")
