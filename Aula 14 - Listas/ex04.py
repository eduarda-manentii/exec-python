# 4. Escreva um programa que leia uma lista com 10 números reais
# mostre-os na ordem inversa.

soremun = []
for c in range(1, 11):
    numero = int(input("Insira o numero {}: ".format(c)))
    soremun.insert(0, numero)

print("Lista de soremun: {}.".format(soremun))
