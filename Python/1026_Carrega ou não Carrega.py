# Lê toda a entrada padrão (stdin), separa em números e converte cada um para inteiro.
dados = map(int, open(0).read().split())

# Cria um iterador explícito sobre 'dados'

it = iter(dados)

# Faz um loop emparelhando os valores de dois em dois usando zip(it, it)
# Esse truque faz com que o primeiro 'it' pegue os números nas posições 0, 2, 4...
# e o segundo 'it' pegue os números nas posições 1, 3, 5...
# Assim, cada iteração retorna um par (a, b)
for a, b in zip(it, it):

    # Faz a operação XOR (OU exclusivo) diretamente entre os inteiros a e b
    # O XOR compara os bits de a e b:
    #   - se forem iguais → resultado = 0
    #   - se forem diferentes → resultado = 1
    resultado = a ^ b  # XOR direto entre inteiros

    # Exibe o resultado na tela.
    print(resultado)
