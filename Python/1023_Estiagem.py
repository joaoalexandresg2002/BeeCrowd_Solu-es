# Lê toda a entrada de uma vez
dados = open(0).read().split()

# Índice para percorrer a lista 'dados'
i = 0

# Contador de cidades
cont = 1

# Lista para armazenar todas as saídas e imprimir de uma vez no final
saida = []

# Loop principal: processa uma cidade por vez
while True:
    # Pega o primeiro valor como número de casas da cidade atual
    n = int(dados[i])
    i += 1  # avança o índice

    # Se for 0, o programa termina
    if n == 0:
        break
    
    # Dicionário para armazenar o consumo médio -> total de pessoas
    consumo = {}

    # Inicializa os totais da cidade
    total_pessoas = total_consumo = 0

    # Loop para ler as informações das 'n' casas
    for _ in range(n):
        # Pega o número de pessoas (p) e o consumo (c)
        p = int(dados[i])
        c = int(dados[i + 1])
        i += 2  # avança 2 posições (pois lemos dois números)

        # Soma nos totais gerais da cidade
        total_pessoas += p
        total_consumo += c

        # Calcula a média de consumo por pessoa (divisão inteira)
        media = c // p

        # Atualiza o dicionário: soma o número de pessoas que têm essa média
        # .get(media, 0) retorna o valor atual ou 0 se ainda não existir
        consumo[media] = consumo.get(media, 0) + p

    # Ordena as chaves (os consumos médios) em ordem crescente
    casas = sorted(consumo)

    # Cria uma lista com o formato "pessoas-consumo" para cada item ordenado
    ordenar = [f"{consumo[casa]}-{casa}" for casa in casas]

    # Calcula o consumo médio total da cidade (sem arredondar pra cima)
    # Multiplicamos por 100 antes da divisão pra preservar 2 casas decimais
    media_consumo = (total_consumo * 100) // total_pessoas / 100

    # Adiciona o resultado formatado da cidade à lista de saídas
    # Note que " ".join(ordenar) junta os pares com espaços
    saida.append(
        f'Cidade# {cont}:\n{" ".join(ordenar)}\nConsumo medio: {media_consumo:.2f} m3.\n'
    )

    # Passa para a próxima cidade
    cont += 1

# Imprime toda a saída de uma vez (evita lentidão com muitos prints)
print("".join(saida))
