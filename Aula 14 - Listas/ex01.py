# Escreva um programa que leia 4 notas e insira em uma lista. Mostre as notas e a média
notas = []
for c in range(1, 5):
    nota = float(input("Insira a nota {}: ".format(c)))
    notas.append(nota)
media = sum(notas) / len(notas)
print("As notas são {} com média de {}.".format(notas, media))
