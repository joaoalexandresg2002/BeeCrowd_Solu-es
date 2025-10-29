# Lê dois números inteiros digitados pelo usuário, separados por espaço
# O primeiro (a) representa o código do produto
# O segundo (b) representa a quantidade comprada
a, b = map(int, input().split())

# Dicionário que associa o código do produto ao seu respectivo preço
# Cada chave (1, 2, 3, 4, 5) é o código do item, e o valor é o preço em reais
precos = {
    1: 4.00,  # Cachorro-quente
    2: 4.50,  # X-salada
    3: 5.00,  # X-bacon
    4: 2.00,  # Torrada simples
    5: 1.50   # Refrigerante
}

# Busca o preço do produto com base no código 'a'
# Se o código não existir no dicionário, retorna 0 (evita erro)
valor = precos.get(a, 0)

# Calcula o total (preço do produto * quantidade) e exibe formatado com duas casas decimais
print(f"Total: R$ {valor * b:.2f}")
