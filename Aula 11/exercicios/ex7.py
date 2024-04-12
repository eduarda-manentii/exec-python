qtde_maior_idade = 0
qtde_menor_idade = 0
for c in range (0, 5):
    numero = int(input("Digite o ano de nascimento: "))
    is_maior_idade = 2024 - numero >= 18
    if(is_maior_idade):
        qtde_maior_idade += 1
    else:
        qtde_menor_idade += 1
print("Maior idade {}".format(qtde_maior_idade))
print("Menor idade {}".format(qtde_menor_idade))
