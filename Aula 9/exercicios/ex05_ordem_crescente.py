# Escreva um programa que leia três números
#  mostre os números em ordem crescente
numero1 = int(input("Digite o número A: "))
numero2 = int(input("Digite o número B: "))
numero3 = int(input("Digite o número C: "))

# FORMA 1 - EU FIZ MAS NÃO APRENDEMOS LISTAS
ordem_numerica = []
ordem_numerica.append(numero1)
ordem_numerica.append(numero2)
ordem_numerica.append(numero3)
ordem_numerica.sort()
print(ordem_numerica)

# FORMA 2 - COMO O PROFESSOR FEZ USANDO O QUE APRENDEMOS EM AULA
maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)
if(numero1 != maior and numero1 != menor):
    print(menor, numero1, maior)
elif(numero2 != maior and numero2 != menor):
    print(menor, numero2, maior)
else:
    print(menor, numero3, maior)
