entrada = map(int, open(0).read().split())  # Lê todos os números inteiros da entrada
e = iter(entrada)                           # Cria um iterador para percorrê-los

while True:                                 # Loop para processar múltiplos casos
    try:
        a = next(e)                         # Primeiro número (valor inicial)
        n = next(e)                         # Segundo número (quantidade de termos)
        while n <= 0:                       # Garante que 'n' seja positivo
            n = next(e)
        
        soma = sum(a + i for i in range(n)) # Soma 'n' números consecutivos a partir de 'a'
        print(soma)                         # Exibe o resultado
    except StopIteration:                   # Encerra o loop ao atingir o fim da entrada
        break
