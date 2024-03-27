import random

numero = int(input("Digite um número de 1 a 10: "))
numero_random = random.randint(1, 10)
if numero == numero_random:
    print("Acertou!")
else:
    print("Errado! O número era {}".format(numero_random))
