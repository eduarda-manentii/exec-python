termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))

for c in range (0, 15 * razao, razao):
    print(c + termo)
