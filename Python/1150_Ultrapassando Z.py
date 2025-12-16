x = int(input())        # Lê o primeiro número inteiro (valor inicial)
z = 0
while z <= x:           # Garante que 'z' seja maior que 'x'
    z = int(input())    # Continua lendo até receber um número maior que 'x'

soma = 0                # Inicializa a soma acumulada
num = x                 # Começa a somar a partir de 'x'
c = 0                   # Contador de quantos números foram somados

while z > soma:         # Continua somando enquanto a soma for menor que 'z'
    soma += num         # Adiciona o número atual à soma
    c += 1              # Conta quantos números foram usados
    num += 1            # Incrementa o número para o próximo valor

print(c)                # Mostra quantos números foram necessários
