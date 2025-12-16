n = int(input())           # Lê a quantidade de termos da sequência de Fibonacci
a, b = 0, 1                # Define os dois primeiros números da sequência
fibonacci = [a, b]         # Cria a lista inicial com 0 e 1

for _ in range(2, n):      # Gera os próximos termos até alcançar 'n'
    a, b = b, a + b        # Atualiza os valores de 'a' e 'b' simultaneamente
    fibonacci.append(b)    # Adiciona o novo número à lista

print(*fibonacci)           # Exibe todos os termos separados por espaço
