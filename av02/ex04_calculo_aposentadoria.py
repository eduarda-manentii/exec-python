# Escreva um programa que leia a idade e o tempo de serviço de um trabalhador
# mostre se ele pode ou não se aposentar. As condições para aposentadoria são:
# Ter pelo menos 65 anos,
# Ou ter trabalhado pelo menos 30 anos,
# Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos

idade = int(input("Digite sua idade: "))
tempo_contribuicao = int(input("Digite seu tempo de contribuição (anos): "))
if (idade >= 60 and tempo_contribuicao >= 25) or (idade >= 65 or tempo_contribuicao >= 30):
    print("Pode se aposentar.")
else:
    print("Não pode se aposentar.")
