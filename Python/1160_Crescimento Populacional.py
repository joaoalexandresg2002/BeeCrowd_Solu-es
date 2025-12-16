e = iter(open(0).read().split()[1:])     # Cria um iterador ignorando o primeiro valor da entrada

for a, b, c, d in zip(e, e, e, e):       # Lê 4 valores por vez: população A, B e taxas
    A = int(a)                           # Converte população A para inteiro
    B = int(b)                           # Converte população B para inteiro
    gA = float(c) / 100                  # Converte taxa de A para decimal
    gB = float(d) / 100                  # Converte taxa de B para decimal

    anos = 0                             # Contador de anos

    # Loop de crescimento das populações
    while A <= B and anos <= 100:        # Continua até A passar B ou completar 100 anos
        A += int(A * gA)                 # A cresce proporcionalmente à sua taxa
        B += int(B * gB)                 # B cresce proporcionalmente à sua taxa
        anos += 1                        # Aumenta 1 ano

    print("Mais de 1 seculo."            # Se passou do limite de 100, imprime essa mensagem
          if anos > 100 
          else f"{anos} anos.")          # Senão, imprime o total de anos necessários
