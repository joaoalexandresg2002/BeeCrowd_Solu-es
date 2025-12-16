for i in range(0, 21, 2):  # i varia de 0 a 20, de 2 em 2
    inicio = 10 + i        # valor base de J para cada I
    # Se i for múltiplo de 10, mostra inteiro; caso contrário, mostra com uma casa decimal
    I_str = str(i // 10) if i % 10 == 0 else f"{i / 10:.1f}"

    for j in (0, 10, 20):  # incrementos de J
        prox = inicio + j  # calcula o valor atual de J
        # Mesmo formato da linha de I
        J_str = str(prox // 10) if prox % 10 == 0 else f"{prox / 10:.1f}"
        print(f"I={I_str} J={J_str}")  # imprime no formato desejado
