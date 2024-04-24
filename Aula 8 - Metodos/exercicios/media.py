nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceiro nota: "))
media = (nota1 + nota2 + nota3) / 3
maior_nota = max(nota1, nota2, nota3)
print("A média é {:.1f} e a maior nota foi {}.".format(media, maior_nota))

if media >= 8:
    print("Aproved")
else:
    print("Not aproved")
