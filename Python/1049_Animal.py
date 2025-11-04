# Lê todas as palavras da entrada, removendo espaços extras com str.strip()
entrada = map(str.strip, open(0).read().split())

# Cria um iterador para percorrer os valores conforme usados
e = iter(entrada)

# Agrupa as palavras de 3 em 3 → cada grupo representa (a, b, c)
# Exemplo: ("vertebrado", "ave", "carnivoro")
for a, b, c in zip(e, e, e):

    # Estrutura de decisão baseada nas 3 palavras
    if a == "vertebrado":
        if b == "ave":
            if c == "carnivoro":
                resposta = "aguia"
            else:
                resposta = "pomba"
        else:  # mamífero
            if c == "onivoro":
                resposta = "homem"
            else:
                resposta = "vaca"
    else:  # invertebrado
        if b == "inseto":
            if c == "hematofago":
                resposta = "pulga"
            else:
                resposta = "lagarta"
        else:  # anelideo
            if c == "onivoro":
                resposta = "minhoca"
            else:
                resposta = "sanguessuga"

    # Exibe o animal identificado
    print(resposta)
