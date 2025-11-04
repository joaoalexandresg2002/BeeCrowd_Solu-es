e = open(0).read().split()  # Lê todos os valores da entrada e separa por espaço

# Extrai os dados de início e fim (dia, hora, minuto e segundo)
dia_inicio, dia_fim = int(e[1]), int(e[8])
hora_inicio, hora_fim = int(e[2]), int(e[9])
minuto_inicio, minuto_fim = int(e[4]), int(e[11])
segundo_inicio, segundo_fim = int(e[6]), int(e[13])

# Converte o momento inicial e final em segundos totais
inicio = (dia_inicio * 86400) + (hora_inicio * 3600) + (minuto_inicio * 60) + segundo_inicio
fim    = (dia_fim * 86400) + (hora_fim * 3600) + (minuto_fim * 60) + segundo_fim

# Calcula o tempo total decorrido em segundos
tempo_segundos = fim - inicio  

# Converte os segundos totais em dias, horas, minutos e segundos restantes
dias, resto = divmod(tempo_segundos, 86400)   # 1 dia = 86400 segundos
horas, resto = divmod(resto, 3600)            # 1 hora = 3600 segundos
minutos, segundos = divmod(resto, 60)         # 1 minuto = 60 segundos

# Exibe o tempo total decorrido no formato solicitado
print(f"{dias} dia(s)")     
print(f"{horas} hora(s)")     
print(f"{minutos} minuto(s)")     
print(f"{segundos} segundo(s)")     
