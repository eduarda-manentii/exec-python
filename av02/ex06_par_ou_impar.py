# Escreva um programa que leia um número
# some 5 caso seja par, ou some 8, caso seja ímpar.
# Mostre o resultado desta operação.

numero = int(input("Digite um número: "))
par = numero % 2 == 0

if(par == True):
    resultado = numero + 5
else:
    resultado = numero + 8
print("O resultado é {}".format(resultado))
