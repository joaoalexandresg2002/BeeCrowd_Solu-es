# Importa a função bisect_left, usada para busca binária eficiente.
from bisect import bisect_left

# Lê toda a entrada padrão de uma vez, separando por espaços e convertendo para inteiros.
dados = map(int, open(0).read().split())

# Cria um iterador a partir da sequência de números.
# Assim podemos ir pegando os valores um a um com next(d), sem precisar usar índices.
d = iter(dados)

# Lista que guardará as saídas formatadas de todos os casos.
saidas = []

# Contador de casos, começa em 1 (como exigido pelo problema).
caso = 1

# Loop principal — cada iteração representa um “caso de teste”.
while True:
    # Pega os dois primeiros números do caso: n = quantidade de mármores, q = número de consultas.
    n, q = next(d), next(d)

    # Condição de parada: se ambos forem 0, o programa termina.
    if (n == 0) and (q == 0):
        break
    
    # Lê os próximos 'n' números — os valores dos mármores — e já os coloca em ordem com sorted().
    marmores = sorted(next(d) for _ in range(n))

    # Lê os próximos 'q' números — os valores a serem consultados (as buscas).
    consultas = [next(d) for _ in range(q)]
    
    # Lista para armazenar as respostas deste caso.
    saida = []

    # Para cada valor a ser consultado (mármore procurado):
    for m in consultas:
        # Usa busca binária para encontrar a posição onde 'm' poderia estar.
        # bisect_left retorna o índice de inserção, ou seja, o ponto onde o valor deveria estar.
        pos = bisect_left(marmores, m)

        # Se a posição for válida e o valor nessa posição for exatamente 'm',
        # então o mármore existe na lista.
        if (pos < len(marmores)) and (marmores[pos] == m):
            saida.append(f'{m} found at {pos + 1}')  # Adiciona ao resultado (posição +1 pois o índice começa em 0)
        else:
            saida.append(f'{m} not found')            # Caso contrário, indica que o mármore não existe.
            
    # Junta as respostas de cada consulta, separando por quebra de linha.
    # Formata também o cabeçalho do caso ("CASE# 1:", etc.)
    saidas.append(f'CASE# {caso}:\n' + "\n".join(saida))

    # Incrementa o número do caso.
    caso += 1     
    

# Ao final, imprime todas as saídas juntas, separadas por uma quebra de linha dupla.
print("\n".join(saidas))
