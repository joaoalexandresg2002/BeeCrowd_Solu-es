# Lê um número inteiro 'n' que indica quantas linhas de texto serão processadas
n = int(input())

# Executa o processamento 'n' vezes
for _ in range(n):

    # Lê uma linha de texto e remove espaços em branco extras nas bordas (início e fim)
    texto = input().strip()

    # Etapa 1: desloca cada letra 3 posições para frente na tabela ASCII
    # - Se o caractere é uma letra (A-Z ou a-z), soma +3 ao seu código (ord)
    # - Caso contrário, mantém o caractere como está
    texto = ''.join(chr(ord(c) + 3) if c.isalpha() else c for c in texto)

    # Etapa 2: inverte toda a string
    texto = texto[::-1]

    # Etapa 3: desloca -1 (para trás) cada caractere da metade em diante
    # - Calcula o ponto médio da string
    tam = len(texto) // 2

    # - Divide a string em duas partes:
    #   1ª metade: permanece igual
    #   2ª metade: cada caractere tem seu código ASCII reduzido em 1
    texto = texto[:tam] + ''.join(chr(ord(c) - 1) for c in texto[tam:])

    # Exibe o texto resultante após as transformações
    print(texto)
