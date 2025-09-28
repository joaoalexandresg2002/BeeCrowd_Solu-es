# Lê uma linha com os dados da primeira peça e separa em partes
# peca1[0] = código da peça
# peca1[1] = quantidade
# peca1[2] = valor unitário
peca1 = input().split(" ")
# Lê uma linha com os dados da segunda peça, no mesmo formato
peca2 = input().split(" ")

# Calcula o valor total da primeira peça
# quantidade (inteiro) * valor unitário (float)
tot_peca1 = int(peca1[1]) * float(peca1[2])
# Calcula o valor total da segunda peça
tot_peca2 = int(peca2[1]) * float(peca2[2])

# Mostra o valor final a pagar (soma dos dois totais), com 2 casas decimais
print(f"VALOR A PAGAR: R$ {tot_peca1 + tot_peca2:.2f}")
