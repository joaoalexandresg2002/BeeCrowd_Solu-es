entrada = map(int, open(0).read().split())  # Lê todos os inteiros da entrada
e = iter(entrada)                           # Cria um iterador para percorrer os valores

# Inicializa contadores
grenais = inter = gremio = empate = 0

# Loop principal — continua até o usuário indicar "2" (não)
while True:
    i, g = next(e), next(e)                 # Lê gols do Inter e do Grêmio
    sair = next(e)                          # Lê a escolha (1 ou 2)
    print("Novo grenal (1-sim 2-nao)")      # Exibe a mensagem a cada rodada

    # Verifica o vencedor da partida
    if i > g:
        inter += 1
    elif i < g:
        gremio += 1
    else:
        empate += 1

    grenais += 1                            # Conta o número total de grenais
    
    if sair == 2:                           # Encerra o loop se o usuário digitar 2
        break

# Exibe o resumo dos resultados
print(f"{grenais} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")

# Determina quem venceu mais
if inter > gremio:
    print("Inter venceu mais")
elif inter < gremio:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
