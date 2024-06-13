arq = open("Aula 27 - Arquivos/teste.txt", "r", encoding='utf-8')
texto = arq.readlines()

for palavra in texto:
    if "2" in palavra:
        print(len(palavra))

i = 1
for frase in texto:
    print("Linha: {}, ocorrências: {}".format(i, frase.count('a')))
    print(len(frase))
    i += 1
