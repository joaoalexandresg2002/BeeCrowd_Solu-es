# Lê um valor inteiro que representa o tempo total em segundos
tempo = int(input())
# Calcula quantas horas cabem dentro do tempo total
# Como 1 hora = 3600 segundos, usamos divisão inteira (//)
hora = tempo // 3600

# Calcula os minutos restantes após remover as horas
# Primeiro pegamos o resto da divisão por 3600 (tempo % 3600),
# depois dividimos por 60 para converter para minutos
minutos = tempo % 3600 // 60

# Calcula os segundos restantes após remover horas e minutos
# Basta pegar o resto da divisão por 60
segundos = tempo % 60

# Imprime no formato pedido: horas:minutos:segundos
print(f"{hora}:{minutos}:{segundos}")
