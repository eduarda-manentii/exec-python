soma_dos_impares = 0
for c in range (0, 6):
    numero = int(input("Digite um número: "))
    is_impar = numero % 2 == 1
    if(is_impar):
        soma_dos_impares = soma_dos_impares + numero
print(soma_dos_impares)
