numero = int(input("Digite o número: "))
contador = 0
for c in range(1, numero+1):
    resto = numero % c
    if(resto == 0) :
        contador += 1
if(contador == 2):
    print("Número primo")
else:
    print("Número não é primo")
