# Lê um número real (ponto flutuante) digitado pelo usuário
n = float(input())

# Cria uma variável 'saida' vazia para armazenar o texto final que será exibido
saida = ""

# Verifica se o número está no intervalo de 0 a 25
if (n >= 0) and (n <= 25):
    saida = "Intervalo [0,25]"

# Caso não esteja no primeiro intervalo, verifica se está entre 25 e 50
    saida = "Intervalo (25,50]"

# Caso não esteja nos anteriores, verifica se está entre 50 e 100
elif (n > 50) and (n <= 100):
    saida = "Intervalo (75,100]"

# Se o número não se encaixar em nenhum intervalo acima, está fora do intervalo considerado
else:
    saida = "Fora de intervalo"

# Exibe o resultado final
print(saida)
