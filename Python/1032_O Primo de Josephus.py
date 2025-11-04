from math import sqrt  # Importa a função sqrt para calcular a raiz quadrada

# Lê todos os números inteiros da entrada padrão
entrada = map(int, open(0).read().split())
e = iter(entrada)

# Loop principal — executa até encontrar o valor 0
while True:
    m = next(e)  # Lê o próximo valor (quantidade de pessoas)
    if m == 0:   # Se for 0, encerra o programa
        break

    primos = []  # Lista que armazenará os números primos gerados
    i = 2        # Primeiro número a testar se é primo

    # Gera os (m - 1) primeiros números primos
    while len(primos) < m - 1:
        v = True  # Assume que o número é primo até provar o contrário
        for j in range(2, int(sqrt(i)) + 1):  # Testa divisores até a raiz de i
            if i % j == 0:  # Se for divisível, não é primo
                v = False
                break
        if v:  # Se continuar sendo primo, adiciona à lista
            primos.append(i)
        i += 1  # Passa para o próximo número

    # Cria uma lista com pessoas numeradas de 1 até m
    pessoas = list(range(1, m + 1))
    pos = 0  # Começa da primeira posição

    # Simula a eliminação com base nos números primos
    for i in range(m - 1):
        pos = (pos + primos[i] - 1) % len(pessoas)  # Calcula quem será eliminado
        pessoas.pop(pos)  # Remove a pessoa eliminada

    # Ao final, sobra apenas uma pessoa → imprime o número dela
    print(pessoas[0])
