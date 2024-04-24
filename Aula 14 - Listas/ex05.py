# 5. Escreva um programa que leia duas listas com 10 itens cada.
# Crie uma terceira lista com 20 itens
# onde os itens serão os itens das duas outras listas intercalados.

lista1 = []
lista2 = []
lista3 = []
for c in range(1, 11):
    numero = input("LISTA 1 -> Insira o item {}: ".format(c))
    lista1.append(numero)

for c in range(1, 11):
    numero = input("LISTA 2 -> Insira o item {}: ".format(c))
    lista2.append(numero)

for c in range(0, 10):
    lista3.append(lista1[c])
    lista3.append(lista2[c])

print("Lista 1: {}.".format(lista1))
print("Lista 2: {}.".format(lista2))
print("Lista de números intercalados: {}.".format(lista3))
