# 2. Escreva um programa para ler os nomes e as notas de cinco alunos e armazenar as
# informações em um dicionário. O programa deverá calcular a média das notas e
# acrescentar essa informação no dicionário

alunos = {}
soma_notas = 0
media = 0

for i in range (0,5):
    numero_aluno = str(i)
    nome_aluno = 'nome' + numero_aluno
    nota_aluno = 'nota' + numero_aluno
    alunos[nome_aluno] = (input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    alunos[nota_aluno] = nota
    soma_notas += nota
    if(i == 4):
        media  = soma_notas / 5
        alunos['media'] = media

print(alunos)

#FORMA BEEM MELHOR
#nome = (input("Digite o nome do aluno: "))
#nota = float(input("Digite a nota do aluno: "))
#notas[nome] = nota
#soma += nota
