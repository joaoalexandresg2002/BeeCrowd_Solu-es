entrada = map(int, open(0).read().split())  # Lê todos os números da entrada
e = iter(entrada)                           # Cria um iterador para percorrer os valores

tipos = {"Alcool": 0, "Gasolina": 0, "Diesel": 0}  # Dicionário para contar os combustíveis

while True:
    tipo = next(e)                          # Lê o próximo tipo de combustível
    while tipo not in [1, 2, 3, 4]:         # Ignora valores inválidos
        tipo = next(e)
    
    if tipo == 4:                           # 4 encerra a leitura
        break
    
    match tipo:                             # Usa 'match' para atualizar o tipo correspondente
        case 1:
            tipos["Alcool"] += 1
        case 2:
            tipos["Gasolina"] += 1
        case _:
            tipos["Diesel"] += 1
            
print("MUITO OBRIGADO")                     # Mensagem final
for nome, qtd in tipos.items():              # Percorre o dicionário e imprime os resultados
    print(f"{nome}: {qtd}")
