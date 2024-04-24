for c in range (0, 5):
    numero = int(input("Digite um número: "))
    if c == 0:
        maior = menor = numero
    if numero > maior_num:
        maior_num = numero
    if numero < menor_num:
        menor_num = numero
print("Maior numero {}".format(maior_num))
print("Menor numero {}".format(menor_num))
