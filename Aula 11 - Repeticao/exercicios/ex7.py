qtde_maior_idade = 0
qtde_menor_idade = 0
for c in range (0, 5):
    ano = int(input("Digite o ano de nascimento: "))
    idade = 2024 - ano
    if(idade >= 18):
        qtde_maior_idade += 1
    else:
        qtde_menor_idade += 1
print("Maior idade {}".format(qtde_maior_idade))
print("Menor idade {}".format(qtde_menor_idade))
