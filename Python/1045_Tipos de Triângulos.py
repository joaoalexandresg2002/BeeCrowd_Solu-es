# Lê três números reais, ordena em ordem decrescente e desempacota em a, b, c
a, b, c = sorted(map(float, input().split()), reverse=True)

# Verifica se a maior medida é maior ou igual à soma das outras duas → não forma triângulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    # Calcula o quadrado de cada lado
    aq, bq, cq = [x ** 2 for x in (a, b, c)]
    soma = bq + cq  # soma dos quadrados dos dois menores lados

    # Classifica o tipo de triângulo quanto aos ângulos
    if aq == soma:
        print("TRIANGULO RETANGULO")      # ângulo reto
    elif aq > soma:
        print("TRIANGULO OBTUSANGULO")    # ângulo obtuso
    else:
        print("TRIANGULO ACUTANGULO")     # ângulos agudos
    
    # Verifica quantos lados distintos existem
    lados = len({a, b, c})
    if lados == 1:
        print("TRIANGULO EQUILATERO")     # três lados iguais
    elif lados == 2:
        print("TRIANGULO ISOSCELES")      # dois lados iguais
