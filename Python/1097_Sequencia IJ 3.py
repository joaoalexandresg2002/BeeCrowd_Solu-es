num = [7, 6, 5]  # Lista inicial com os valores de J

# Loop de I indo de 1 até 9 (inclusive), com passo 2 → 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    # Loop interno percorre os três índices da lista num
    for j in range(3):
        print(f"I={i} J={num[j]}")  # Exibe o valor atual de I e J
        num[j] += 2                 # Incrementa o valor de J em 2 após imprimir
