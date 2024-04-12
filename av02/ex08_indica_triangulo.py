# Escreva um programa que leia três valores inteiros.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é:
# equilátero, isósceles ou escaleno.

numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Digite o número 2: "))
numero3 = int(input("Digite o número 3: "))

opcao1 = numero2 + numero3
opcao2 = numero1 + numero3
opcao3 = numero1 + numero2

lado1_igual = numero1 == numero2
lado2_igual = numero2 == numero3
lado3_igual = numero1 == numero3

lado1_diferente = numero1 != numero2
lado2_diferente = numero2 != numero3
lado3_diferente = numero1 != numero3

if (opcao1 > numero1) and (opcao2 > numero2) and (opcao3 > numero3):
    if(numero1 == numero2 == numero3):
        print("É um triângulo Equilátero.")
    else:
        if(lado1_igual or lado2_igual or lado3_igual):
            print("É um triângulo Isósceles.")
        else:
            print("É um triângulo Escaleno.")
else:
    print("Não é um triangulo.")
