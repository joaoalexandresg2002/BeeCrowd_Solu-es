# Lê toda a entrada padrão
entrada = map(int, open(0).read().split())

# Cria um iterador a partir da sequência de números lidos
# Isso permite consumir os valores aos poucos conforme o loop avança
e = iter(entrada)

# Usa zip(e, e) para agrupar os números de dois em dois
for a, b in zip(e, e):

    # A linha abaixo usa uma expressão condicional (operador ternário em Python)
    # Verifica se os números são múltiplos entre si:
    #  - Se b % a == 0 ou a % b == 0 → São múltiplos
    #  - Caso contrário → Não são múltiplos
    print("Sao Multiplos" if b % a == 0 or a % b == 0 else "Nao sao Multiplos")
