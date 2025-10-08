# Importa a classe Fraction da biblioteca padrão fractions
# Ela permite representar frações de forma exata e faz simplificação automática.
from fractions import Fraction

# Lê um número inteiro que representa quantas expressões serão processadas.
n = int(input())

# Loop para processar as N expressões
for i in range(n):
    # Lê a linha da entrada e separa em partes (tokens).
    # Exemplo: "1 / 2 + 3 / 4" -> ["1", "/", "2", "+", "3", "/", "4"]
    expressao = list(map(str, input().split()))
    
    # Extrai numerador e denominador da primeira fração
    n1, d1 = int(expressao[0]), int(expressao[2])
    
    # Extrai o sinal da operação (+, -, *, /)
    s = expressao[3]
    
    # Extrai numerador e denominador da segunda fração
    n2, d2 = int(expressao[4]), int(expressao[6])
    
    # Por padrão, o denominador final será d1 * d2 (caso de +, - e *)
    denominador = d1 * d2
    
    # Verifica qual operação deve ser feita
    if s == "+":  # Soma de frações
        # Fórmula: a/b + c/d = (a*d + b*c) / (b*d)
        numerador = n1 * d2 + d1 * n2
    elif s == "-":  # Subtração de frações
        # Fórmula: a/b - c/d = (a*d - b*c) / (b*d)
        numerador = n1 * d2 - d1 * n2
    elif s == "*":  # Multiplicação de frações
        # Fórmula: a/b * c/d = (a*c) / (b*d)
        numerador = n1 * n2
    else:  # Divisão de frações
        # Fórmula: (a/b) ÷ (c/d) = (a*d) / (b*c)
        numerador = n1 * d2
        denominador = n2 * d1  # aqui o denominador muda
    
    # Cria a fração simplificada automaticamente
    fracao = Fraction(numerador, denominador)
    
    # Imprime a versão "não simplificada" e a versão "simplificada"
    print(f"{numerador}/{denominador} = {fracao.numerator}/{fracao.denominator}")
