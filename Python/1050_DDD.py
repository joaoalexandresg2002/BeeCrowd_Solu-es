try:
    n = int(input())  # Lê o DDD informado pelo usuário

    # Dicionário que associa DDDs às cidades correspondentes
    ddd = {
        61: "Brasilia",
        71: "Salvador",
        11: "Sao Paulo",
        21: "Rio de Janeiro",
        32: "Juiz de Fora",
        19: "Campinas",
        27: "Vitoria",
        31: "Belo Horizante"
    }

    print(ddd[n])  # Imprime o nome da cidade correspondente ao DDD informado

# Caso o DDD não esteja no dicionário, ocorre KeyError
except KeyError:
    print("DDD nao cadastrado")  # Exibe mensagem informando que o DDD não existe
