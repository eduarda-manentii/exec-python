# 2. Escreva  um programa que leia 10 números inteiros e insira em uma lista.
# Crie uma lista com os números pares e uma outra lista com os números ímpares.
# Mostre as três listas.

numeros = []
numeros_pares = []
numeros_impares = []
for c in range(1, 11):
    numero = int(input("Insira o numero {}: ".format(c)))
    numeros.append(numero)
    resto = numero % 2
    if(resto > 0):
        numeros_impares.append(numero)
    else:
        numeros_pares.append(numero)
print("Lista de números geral: {}.".format(numeros))
print("Lista de números pares: {}.".format(numeros_pares))
print("Lista de números impares: {}.".format(numeros_impares))
