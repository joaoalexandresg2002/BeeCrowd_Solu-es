# Lê o valor de dinheiro em ponto flutuante (ex: 576.73)
dinheiro = float(input())

# Lista das notas disponíveis em reais
notas = [100, 50, 20, 10, 5, 2]

print("NOTAS:")
# Para cada nota, calcula quantas cabem no valor
for nota in notas:
    # Divide o valor pelas notas e mostra a quantidade
    # :.0f -> formata para número inteiro (sem casas decimais)
    print(f"{dinheiro // nota:.0f} nota(s) de R$ {nota}.00")
    # Atualiza o valor de 'dinheiro' com o que sobra após usar essas notas
    dinheiro %= nota

# Lista das moedas em centavos (100 = R$1.00, 50 = R$0.50, etc.)
moedas = [100, 50, 25, 10, 5, 1]

print("MOEDAS:")
# Converte o valor que sobrou em centavos para evitar erro de ponto flutuante
dinheiro_centavos = dinheiro * 100

# Para cada moeda em centavos
for moeda in moedas:
    # Calcula quantas moedas cabem
    print(f"{dinheiro_centavos // moeda:.0f} moeda(s) de R$ {moeda / 100:.2f}")
    # Atualiza o valor em centavos com o resto
    dinheiro_centavos %= moeda
