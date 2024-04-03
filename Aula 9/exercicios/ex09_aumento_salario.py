# Escreva um programa que leia o salário de um funcionário e calcule o valor do seu
# aumento. Para salários acima de R$ 1340,00 calcule um aumento de 10%. Para
# valores abaixo ou igual, o aumento será de 15%
salario_atual = float(input("Digite o salário atual: "))
if(salario_atual > 1340):
    aumento = salario_atual * 10/100
else:
    aumento = salario_atual * 15/100
salario_com_reajuste = salario_atual + aumento
print("O novo salário do funcionário é de R${}.".format(salario_com_reajuste))
