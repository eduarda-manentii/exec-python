# 4. Escreva um programa que leia uma lista com 10 números reais
# mostre-os na ordem inversa.

soremun = []
for c in range(1, 11):
    numero = int(input("Insira o numero {}: ".format(c)))
    soremun.append(numero)

for c in range(10, 0, -1):
    print(soremun[c-1])
