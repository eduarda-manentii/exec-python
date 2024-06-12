# 2. Escreva um programa que leia um número entre 0 e 9999 e mostre a composição desse número
# (cada um dos dígitos separados).
#  Exemplo: 2468
#  unidade: 8
#  dezena: 6
#  centena: 4
#  milhar: 2

numero = input("Digite um numero: ")
tam = len(numero)
if(tam >= 1) and (tam <= 4):
    print("Unidade: {} ".format(numero[tam-1]))
    if(tam >= 2):
        print("Dezena: {} ".format(numero[tam-2]))
        if(tam >= 3):
          print("Centena: {} ".format(numero[tam-3]))
        else:
           print("Milhar: {} ".format(numero[tam-4]))
else:
    print("Número fora do range permitdo.")
