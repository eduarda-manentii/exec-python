# Escreva um programa para aprovar um financiamento para compra de um imóvel.
# O programa deve ler o valor do imóvel, o salário e a quantidade de meses a pagar.
# Calcule o valor da prestação como sendo o valor do imóvel
# dividido pelo número de meses a pagar. O valor da prestação mensal
# não pode ser superior a 30% do salário.

valor_imovel = float(input("Digite o valor do imóvel: "))
salario = float(input("Digite o salário: "))
meses_a_pagar = int(input("Digite a quantidade de meses a pagar: "))

prestacao = valor_imovel / meses_a_pagar
salario_correspondente = salario * 30/100

if(prestacao > salario_correspondente):
    print("Não é possível aprovar o financiamento.")
else:
   print("Financiamento aprovado.")
