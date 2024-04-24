# Escreva um programa que leia 8 números inteiros
# mostre a quantidade de números pares e a quantidade de números ímpares

contador_par = 0
contador_impar = 0
for c in range (0, 8):
    numero = int(input("Digite um número inteiro: "))
    resto = numero % 2
    if(resto > 0):
        contador_impar += 1
    else:
        contador_par += 1
print("Quantidade de números pares: {} ".format(contador_par))
print("Quantidade de números impares: {}".format(contador_impar))
