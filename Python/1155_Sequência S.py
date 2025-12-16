a = 2             # Numerador inicial da fração
b = 3             # Denominador inicial da fração
soma = 0          # Acumulador da soma das frações

while int(soma) != 519:    # Continua até que a parte inteira da soma seja 519
    soma += a / b          # Soma a fração atual (a dividido por b)
    a += 2                 # Incrementa o numerador em 2
    b += 2                 # Incrementa o denominador em 2

print(int(soma) / 100)     # Imprime o valor final dividido por 100
