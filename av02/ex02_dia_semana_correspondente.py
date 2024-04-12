# Escreva um programa que leia um número e mostre o dia correspondente da semana.
# (1-domingo, 2- segunda, etc.)
# se digitar outro valor deve aparecer “valor inválido”.

numero = int(input("Digite um número: "))
if(numero <= 0 or numero > 7):
    print("Valor inválido.")
if(numero == 1):
    print("Domingo.")
if(numero == 2):
    print("Segunda.")
if(numero == 3):
    print("Terça.")
if(numero == 4):
    print("Quarta.")
if(numero == 5):
    print("Quinta.")
if(numero == 6):
    print("Sexta.")
if(numero == 7):
    print("Sábado.")
