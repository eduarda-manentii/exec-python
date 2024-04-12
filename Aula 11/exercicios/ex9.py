idade = 0
for c in range (1, 5):
    numero = int(input("Digite a idade: "))
    idade = idade + numero
    if(c >= 4):
        idade = idade / 4


print("Media de idade {}".format(idade))
