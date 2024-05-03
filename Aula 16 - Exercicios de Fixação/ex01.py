# 1. Escreva um programa que leia o nome completo de uma pessoa e mostre:
# ○	o nome com todas as letras maiúsculas
# ○	o nome com todas as letras minúsculas
# ○	Quantas letras (sem considerar os espaços)
# ○	Quantas letras tem o primeiro nome

nome_completo = input("Digite o nome completo: ")

partes_nome = nome_completo.split()
espacos = nome_completo.count(" ")

print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo) - espacos)
print(partes_nome[0])
