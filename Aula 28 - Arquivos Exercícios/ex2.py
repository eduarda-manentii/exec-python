# Escreva um programa que mostre duas opções para o usuário: (1) Cadastrar uma pessoa ou (2) Listar
# pessoas cadastradas. Os nomes deverão ser armazenados em um arquivo texto.

leitura_arquivo = open("Aula 28 - Arquivos Exercícios/pessoas.txt", "r", encoding='utf-8')
escrita_arquivo = open("Aula 28 - Arquivos Exercícios/pessoas.txt", "a+", encoding='utf-8')

print("O que deseja?\n 1 - Cadastrar pessoas\n 2 - Listar pessoas")
opcao = int(input("Opção escolhida: "))

if(opcao == 1):
    pessoa = input("Digite o nome da pessoa: ")
    escrita_arquivo.write(pessoa)
    print("Pessoa adicionada com sucesso.\n")
elif(opcao == 2):
    linhas = leitura_arquivo.readlines()
    for linha in linhas:
        print(linha + "\n")
else:
    print("Opção inválida.")
