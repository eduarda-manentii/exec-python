# Escreva um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário. No final coloque esse
# dicionário em ordem, sabendo que o vencedor tirou o maior número.

import random

jogadores = {"Jogador 1" : random.randint(1, 6), "Jogador 2" : random.randint(1, 6), "Jogador 3" : random.randint(1, 6), "Jogador 4" : random.randint(1, 6)}

# FORMA QUE EU FIZ
lista = []
for i in sorted(jogadores, key = jogadores.get):
    lista.append(str(i) + " -> Número: " + str(jogadores[i]))

for jogador in range (len(lista), 0, -1):
    print(lista[jogador - 1])

# FORMA MELHOR
for i in sorted(jogadores, key = jogadores.get, reverse=True):
    print(i, [jogadores[i]])
