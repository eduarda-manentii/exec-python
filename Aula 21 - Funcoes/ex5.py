#5.	Escreva um programa que leia o nome de uma pessoa e chame uma
# função para retornar o nome invertido com letras maiúsculas.

def retorna_nome_maiusculo(nome):
    return nome[::-1].upper()

print(retorna_nome_maiusculo("duda"))
