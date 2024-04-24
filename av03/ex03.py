# Escreva um programa que leia um número inteiro.
# Se esse número for positivo, calcule a raiz quadrada do número.
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

import math

numero = int(input("Digite um número: "))
if(numero >= 0):
   print("A raiz quadrada do número {} é {}.".format(numero, math.sqrt(numero)))
else:
    print("O número é inválido.")
