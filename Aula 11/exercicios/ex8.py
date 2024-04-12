maior_num = 0
menor_num = 0
for c in range (0, 5):
    numero = int(input("Digite um número: "))
    if(maior_num == 0 or menor_num == 0):
        maior_num = numero
        menor_num = numero
    else:
        is_maior = numero > maior_num
        is_menor = numero < menor_num
        if(is_maior):
            maior_num = numero
        elif(is_menor):
            is_menor = numero

print("Maior numero {}".format(maior_num))
print("Menor numero {}".format(menor_num))
