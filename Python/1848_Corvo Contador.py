e = list(open(0).read().splitlines())  # Lê todas as linhas da entrada
soma = 0                               # Acumulador do valor dos gritos

for v in e:                            # Percorre cada linha da entrada
    if v != "caw caw":                 # Se não for o comando de impressão
        # Converte '-' em 0 e qualquer outro símbolo em 1
        num = ["0" if i == "-" else "1" for i in v]
        soma += int(''.join(num), 2)   # Converte binário para inteiro e soma
    else:
        print(soma)                    # Imprime a soma acumulada
        soma = 0                       # Reinicia a soma para o próximo caso
