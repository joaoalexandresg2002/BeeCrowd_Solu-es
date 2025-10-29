x, y = map(float, input().split())

# Verifica a posição do ponto em relação aos eixos
if x == 0 and y == 0:
    ponto = "Origem"
elif x == 0:
    ponto = "Eixo Y"
elif y == 0:
    ponto = "Eixo X"
elif x > 0 and y > 0:
    ponto = "Q1"
elif x < 0 and y > 0:
    ponto = "Q2"
elif x < 0 and y < 0:
    ponto = "Q3"
else:  # x > 0 and y < 0
    ponto = "Q4"
print(ponto)
