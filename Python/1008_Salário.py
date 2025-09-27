# Lê o número de identificação do funcionário (pode ser tratado como texto)
num_func = input()
# Lê a quantidade de horas trabalhadas (valor inteiro)
num_hr_trab = int(input())
# Lê o valor recebido por hora (pode ter casas decimais)
valor_hora = float(input())

# Mostra o número do funcionário
print("NUMBER =", num_func)

# Calcula o salário multiplicando horas trabalhadas pelo valor da hora
# e exibe formatado com 2 casas decimais
print(f"SALARY = U$ {num_hr_trab * valor_hora:.2f}")
