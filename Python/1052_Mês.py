n = int(input())  # Lê um número inteiro que representa o mês

# Dicionário que associa números (1 a 12) aos nomes dos meses em inglês
mes = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

print(mes[n])  # Imprime o nome do mês correspondente ao número informado
