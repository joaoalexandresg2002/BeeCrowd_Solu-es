# Lê todos os números inteiros da entrada padrão
entrada = map(int, open(0).read().split())

# Cria um iterador para percorrer os valores
e = iter(entrada)

# Lê o primeiro valor, que indica o número de casos de teste
c = next(e)

# Lista para armazenar todas as saídas formatadas
saida = []

# Loop que executa para cada caso de teste
for i in range(1, c + 1):
    # Lê os valores n (quantidade de pessoas) e k (passos de eliminação)
    n, k = next(e), next(e)

    # Cria uma lista de pessoas numeradas de 1 até n
    pessoas = list(range(1, n + 1))

    # Define a posição inicial como 0 (primeira pessoa)
    pos = 0

    # Enquanto houver mais de uma pessoa, continua eliminando
    while len(pessoas) > 1:
        # Calcula a posição da próxima pessoa a ser eliminada
        pos = (pos + k - 1) % len(pessoas)
        # Remove a pessoa da lista
        pessoas.pop(pos)

    # Armazena o resultado no formato "Case X: Y"
    saida.append(f"Case {i}: {pessoas[0]}")

# Imprime todos os resultados, um por linha
print("\n".join(saida))
