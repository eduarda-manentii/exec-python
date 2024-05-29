# 1 - Escreva um programa que leia nome e média de um aluno, guardando também a
# situação em um dicionário. Ao final mostre o conteúdo da estrutura na tela.

nome = input("Digite seu nome: ")
media = float(input("Digite sua média: "))
situacao = ""
if (media > 6):
    situacao = "aprovado"
else:
    situacao = "reprovado"

aluno = {"nome" : nome, "media" : media, "situacao" : situacao}

print(aluno['nome'])
print(aluno['media'])
print(aluno['situacao'])
