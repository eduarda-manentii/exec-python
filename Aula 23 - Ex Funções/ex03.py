# 3. Escreva um programa que leia nome, ano de nascimento e número da carteira de
# trabalho. Armazene esses dados, junto com a idade, em um dicionário. Se o
# número da carteira de trabalho for diferente de zero, o dicionário receberá também o
# ano de contratação e o salário

nome = input("Digite seu nome: ")
nasc = int(input("Digite o ano do seu nascimento: "))
carteira = int(input("Digite o número da carteira de trabaio: "))

idade = 2024 - nasc
trabalhador = {
    "nome" : nome,
    "nasc" : nasc,
    "carteira_trabalho" : carteira,
    "idade" : idade
    }
carteira = (carteira != 0)
if(carteira):
    ano_contratacao = int(input("Digite o ano de contratação: "))
    trabalhador['ano_contratacao'] = ano_contratacao
    salario = float(input("Digite o salário: "))
    trabalhador['salario'] = salario

print(trabalhador['nome'])
print(trabalhador['nasc'])
print(trabalhador['carteira_trabalho'])
print(trabalhador['idade'])
if (carteira):
    print(trabalhador['ano_contratacao'])
    print(trabalhador['salario'])
