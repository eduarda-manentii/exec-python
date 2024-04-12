# Escreva um programa que leia três números: n1, n2, n3
# mostre se a soma de n1 + n2 é menor que n3.

numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))
numero3 = float(input("Digite o número 3: "))

resultado_soma = numero1 + numero2
if(resultado_soma < numero3):
    print("O resultado entre a soma de {} mais {} é menor que {}".format(numero1, numero2, numero3))
