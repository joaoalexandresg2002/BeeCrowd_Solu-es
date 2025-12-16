num = [7, 6, 5]  # Lista com os valores fixos de J a serem usados no padrão

# Loop de I variando de 1 até 9, pulando de 2 em 2 (1, 3, 5, 7, 9)
for i in range(1, 10, 2):
    # Loop interno percorre os três valores da lista num2
    for j in range(3):
        print(f"I={i} J={num[j]}")  # Exibe o par I e J conforme o padrão pedido
