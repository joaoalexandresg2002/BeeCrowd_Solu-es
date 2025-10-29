# Lê toda a entrada padrão
entrada = map(int, open(0).read().split())

# Cria um iterador (objeto que pode ser percorrido) a partir da sequência 'entrada'
# Isso permite avançar pelos elementos conforme são consumidos
e = iter(entrada)

# Usa 'zip(e, e, e)' para agrupar os números de 3 em 3
# → O primeiro grupo será (a1, b1, c1), depois (a2, b2, c2), etc.
# Exemplo: se a entrada for "7 21 -14 3 -7 8"
# então teremos: (7, 21, -14) e (3, -7, 8)
for a, b, c in zip(e, e, e):

    # Cria uma lista com os três números do grupo
    num = [a, b, c]

    # Cria uma nova lista com os mesmos números, mas ordenados em ordem crescente
    ordenado = sorted(num)
    
    # Imprime os números ordenados, um por linha
    # O operador '*' "desempacota" a lista, imprimindo cada elemento separadamente
    print(*ordenado, sep="\n")

    # Imprime uma linha em branco para separar os blocos
    print()

    # Imprime novamente os números originais (na ordem que foram digitados)
    print(*num, sep="\n")
