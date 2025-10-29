entrada = map(float, open(0).read().split())
e = iter(entrada)

while True:
    try:
        # Lê as 4 notas
        notas = [next(e) for _ in range(4)]
        pesos = [2, 3, 4, 1]
        
        # Média ponderada
        media = sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)
        print(f"Media: {media:.1f}")

        # Avaliação inicial
        if media >= 7.0:
            print("Aluno aprovado.")
        elif media < 5.0:
            print("Aluno reprovado.")
        else:
            print("Aluno em exame.")
            
            # Lê nota do exame
            nota_exame = next(e)
            print(f"Nota do exame: {nota_exame:.1f}")

            media_final = (media + nota_exame) / 2
            if media_final >= 5.0:
                print("Aluno aprovado.")
            else:
                print("Aluno reprovado.")
            print(f"Media final: {media_final:.1f}")

    except StopIteration:
        break
