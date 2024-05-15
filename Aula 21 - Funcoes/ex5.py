#5.	Escreva um programa que leia o nome de uma pessoa e chame uma
# função para retornar o nome invertido com letras maiúsculas.

def retorna_nome_maiusculo(nome):
    nome_maiusculo = nome.upper()
    emon = ""
    for c in range (len(nome_maiusculo), 0, -1):
        emon += nome_maiusculo[c - 1]
    return emon

print(retorna_nome_maiusculo("duda"))
