arq = open("Aula 27 - Arquivos/teste2.txt", "w+", encoding='utf-8')
linhas = ['linha 1', 'linha 2', 'linha 3', 'linha 4', 'linha 5', 'linha 6']

for linha in linhas:
    arq.write(linha)
    arq.write("\n")
