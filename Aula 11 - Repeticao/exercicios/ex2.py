soma = 0
for c in range (0, 100):
    par = c % 2 == 0
    if(par):
        soma = soma + c
print(soma)
