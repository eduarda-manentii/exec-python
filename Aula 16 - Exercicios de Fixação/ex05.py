# 5. Escreva um programa que leia o nome completo de uma pessoa
# mostre o primeiro e último nome separadamente.

nome_completo = input("Digite o nome completo: ")
partes_nome = nome_completo.split()
qtde_partes = len(partes_nome)
print("Primeiro nome: {} ".format(partes_nome[0]))
print("Segundo nome: {} ".format(partes_nome[qtde_partes-1]))
