# Escreva um programa que leia a idade de uma pessoa
# mostre a classificação de acordo com as faixas de idades:
#	Criança para 0 até 11 anos;
#	Adolescente para 12 até 18 anos;
#	Jovem para 19 até 24 anos;
#	Adulto para 25 até 40 anos;
#	Meia Idade para 41 até 60 anos;
#	Idoso acima de 60 anos.

idade = int(input("Digite sua idade: "))
if(idade >= 0 and idade <= 11):
    print("Criança.")
if(idade >= 12 and idade <= 18):
    print("Adolescente.")
if(idade >= 19 and idade <= 24):
    print("Jovem.")
if(idade >= 25 and idade <= 40):
    print("Adulto.")
if(idade >= 41 and idade <= 60):
    print("Meia Idade.")
if(idade > 60):
    print("Idoso.")
