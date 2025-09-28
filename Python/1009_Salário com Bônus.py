# Lê o nome do vendedor e remove espaços extras no começo ou fim (strip)
nome_vend = input().strip()
# Lê o salário fixo do vendedor
sal_vend = float(input())

# Lê o total de vendas realizadas pelo vendedor
tot_vendas = float(input())

# Calcula o salário final adicionando 15% sobre o valor das vendas
# e exibe o resultado formatado com 2 casas decimais
print(f"TOTAL = R$ {sal_vend + tot_vendas * 0.15:.2f}")
