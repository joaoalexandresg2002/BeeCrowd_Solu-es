i = 1  # Valor inicial de I

# Loop decrescente de J, começando em 60 e indo até 0 (inclusive), de 5 em 5
for j in range(60, -1, -5):
    print(f"I={i} J={j}")  # Exibe os valores atuais de I e J
    i += 3                 # Incrementa I em 3 a cada iteração
