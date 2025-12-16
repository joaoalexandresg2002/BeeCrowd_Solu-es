entrada = map(int, open(0).read().split())  # Lê todos os números inteiros da entrada
e = iter(entrada)                           # Cria um iterador para percorrer os valores em pares

# Percorre os números de dois em dois (n e m)
for valor in zip(e, e):
    n, m = sorted(valor)  # Ordena para garantir que n < m

    # Interrompe o loop se algum dos números for menor ou igual a 0
    if (n <= 0) or (m <= 0):
        break

    soma = 0  # Armazena a soma dos números do intervalo

    # Percorre todos os números de n até m (inclusive)
    for i in range(n, m + 1):
        print(i, end=" ")  # Imprime os números lado a lado na mesma linha
        soma += i          # Soma o valor atual

    # Exibe a soma total ao final da linha
    print(f"Sum={soma}")
