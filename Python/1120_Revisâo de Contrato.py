# Lê toda a entrada e cria um iterador
dados = iter(open(0).read().split())

for a, b in zip(dados, dados):
    if a == b == "0":
        break

    # Usa filter() para remover o caractere 'a' de 'b'
    resultado = ''.join(filter(lambda x: x != a, b)).lstrip('0')
    
    # Imprime "0" se o resultado for vazio
    print(resultado or "0")
