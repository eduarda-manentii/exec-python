# 6. Duas listas foram criadas com idades e alturas de 10 alunos.
# Escreva um programa que mostre quantos alunos com mais de 11 anos
# possuem altura inferior à média de altura desses alunos

idades = [10, 15, 10, 4, 5, 48, 19, 20, 11, 11]
alturas = [150, 170, 140, 130, 172, 182, 179, 145, 160, 200]
media_altura = sum(alturas) / len(idades)
contador = 0
for c in range(0, 10):
    if(idades[c] > 11):
        altura = alturas[c]
        if(altura < media_altura):
            contador += 1

print("Existem {} alunos com mais de 11 anos que possuem altura inferior á média de {}.".format(contador, media_altura))
