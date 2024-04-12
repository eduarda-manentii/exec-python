numero = int(input("Digite o número: "))
qntde = 0
for c in range(1, numero):
    if(numero > 1 and numero % c == 0) :
        qntde += 1

if(qntde == 1):
    print("Número primo")
else:
    print("Número não é primo")
