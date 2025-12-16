e = iter(open(0).read().split()[1:])   # Lê a entrada ignorando o primeiro valor e cria um iterador

pd = "pedra"     # Define a opção "pedra"
pp = "papel"     # Define a opção "papel"
ts = "tesoura"   # Define a opção "tesoura"
lg = "lagarto"   # Define a opção "lagarto"
sp = "Spock"     # Define a opção "Spock"

ganha = {        # Dicionário que indica quais opções cada jogada vence
    pd: {ts, lg},
    pp: {pd, sp},
    ts: {pp, lg},
    lg: {pp, sp},
    sp: {pd, ts}    
}

cont = 1         # Contador de casos
for s, r in zip(e, e):  # Lê pares de jogadas (Sheldon e Raj)
    s.strip()           # Remove espaços extras da jogada de Sheldon
    r.strip()           # Remove espaços extras da jogada de Raj
    
    if s == r:          # Se as jogadas forem iguais
        resp = "De novo!"
    elif r in ganha[s]: # Se Sheldon vence Raj
        resp = "Bazinga!"
    else:               # Caso contrário, Raj vence
        resp = "Raj trapaceou!"
        
    print(f"Caso #{cont}: {resp}")  # Imprime o resultado do caso
    cont += 1                        # Incrementa o contador
