# 3. Escreva um programa que leia uma lista com cinco números inteiros
# mostre a soma, a multiplicação e os números.
numeros = []
total_multiplicacao = 1
total_soma = 0
for c in range(1, 6):
    numero = int(input("Insira o numero {}: ".format(c)))
    numeros.append(numero)
    total_soma += numero
    total_multiplicacao = total_multiplicacao * numero
print("Lista de números geral: {}.".format(numeros))
print("Soma total dos números: {}.".format(total_soma))
print("Multlicação total dos números: {}.".format(total_multiplicacao))
