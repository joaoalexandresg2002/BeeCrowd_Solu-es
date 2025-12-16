e = iter(map(int, open(0).read().split()))   # Cria um iterador com todos os valores da entrada

for valor in e:                               # Percorre cada número fornecido
    print("vai ter copa!" if valor == 0       # Se o valor for 0 → imprime "vai ter copa!"
          else "vai ter duas!")              # Caso contrário → "vai ter duas!"
