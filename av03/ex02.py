# Escreva um programa que leia 2 números inteiros
# mostre os números que estão no intervalo entre eles.

numero1 = int(input("Digite o valor do primeiro número: "))
numero2 = int(input("Digite o valor do segundo número: "))

for c in range (numero1+1, numero2):
    print(c)
