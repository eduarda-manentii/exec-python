# Escreva um programa para ler um número inteiro
# mostrar na tela se o número é par ou ímpar
numero = int(input("Digite um número: "))
valor = numero % 2 == 1
if(valor == True):
    print("O valor é impar.")
else:
    print("O valor é par.")
