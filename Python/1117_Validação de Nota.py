entrada = map(float, open(0).read().split())  # Lê todos os valores como float
e = iter(entrada)                             # Cria um iterador para percorrer as notas

soma = 0                                      # Acumula a soma das notas válidas
c = 0                                         # Conta quantas notas válidas já foram lidas

# Continua até receber 2 notas válidas
while c < 2:
    num = next(e)                             # Lê a próxima nota
    if 0 <= num <= 10:                        # Verifica se a nota é válida
        soma += num                           # Soma a nota
        c += 1                                # Conta a nota válida
    else:
        print("nota invalida")                # Exibe mensagem se for inválida

# Exibe a média das duas notas válidas com duas casas decimais
print(f"media = {soma / 2:.2f}")
