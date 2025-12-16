# Dicionário que associa cada dígito ao número de LEDs necessários para exibi-lo
leds = {
    "1": 2, "2": 5, "3": 5, "4": 4, "5": 5,
    "6": 6, "7": 3, "8": 7, "9": 6, "0": 6
}

entrada = open(0).read().split()  # Lê toda a entrada e separa por espaço/linha

# Ignora o primeiro valor (quantidade de casos) e percorre os números seguintes
for numero in entrada[1:]:
    # Soma a quantidade de LEDs necessários para cada dígito do número
    soma = sum(leds[d] for d in numero)

    # Exibe o total de LEDs usados para formar o número
    print(f"{soma} leds")
