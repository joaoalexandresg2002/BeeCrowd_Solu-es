entrada = map(int, open(0).read().split())  # Lê todos os números inteiros da entrada
e = iter(entrada)                           # Cria um iterador para percorrer os valores
senha = 2002                                # Define a senha correta

# Percorre cada valor digitado
for valor in e:
    if valor == senha:                      # Se o valor for igual à senha correta
        print("Acesso Permitido")           # Exibe mensagem de sucesso
        break                               # Interrompe o loop
    else:
        print("Senha Invalida")             # Caso contrário, exibe erro
