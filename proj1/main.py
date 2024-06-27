import re
from collections import Counter
from temas import temas

def carregar_palavras_comuns(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        palavras_comuns = set(f.read().split())
    return palavras_comuns

def remover_palavras_comuns(palavras, palavras_comuns):
    palavras_filtradas = [palavra for palavra in palavras if palavra not in palavras_comuns]
    return palavras_filtradas

def contar_frequencia(palavras):
    contador = Counter(palavras)
    return contador

def associar_tema(palavras_mais_comuns):
    contagem_temas = Counter()
    for palavra, _ in palavras_mais_comuns:
        for tema, palavras_associadas in temas.items():
            if palavra in palavras_associadas:
                contagem_temas[tema] += 1
    tema_principal = contagem_temas.most_common(1)
    if tema_principal:
        return tema_principal[0][0]
    else:
        return "não foi possível determinar o tema principal"

def gerar_resumo(contador):
    palavras_mais_comuns = contador.most_common(5)
    tema = associar_tema(palavras_mais_comuns)
    palavras_mais_usadas = [palavra for palavra, _ in palavras_mais_comuns]
    return tema, palavras_mais_usadas

def extrair_palavras(texto):
    padrao = r'\b[\wà-úÀ-ÚãõÃÕáéíóúÁÉÍÓÚçÇüÜ]+\b'
    palavras = re.findall(padrao, texto.lower())
    return palavras

def extrair_caracteres(texto):
    qtde_espacos = texto.count(" ")
    tam_texto = len(texto)
    caracteres_sem_espaco = tam_texto - qtde_espacos
    return tam_texto, caracteres_sem_espaco

texto = input("Digite um texto: ").lower()
tam_texto, caracteres_sem_espaco = extrair_caracteres(texto)
qtde_palavras = extrair_palavras(texto)

palavras_comuns = carregar_palavras_comuns("proj1/palavras_comuns.txt")
palavras_filtradas = remover_palavras_comuns(qtde_palavras, palavras_comuns)
contador = contar_frequencia(palavras_filtradas)
tema, palavras_mais_usadas = gerar_resumo(contador)

print("Quantidade de caracteres excluindo espaços: {}".format(caracteres_sem_espaco))
print("Quantidade de caracteres: {}".format(tam_texto))
print("Quantidade de palavras: {}".format(len(qtde_palavras)))
print("Cinco palavras mais usadas: {}".format(", ".join(palavras_mais_usadas)))
print("Tema do texto, determinado nas palavras mais usadas: {}".format(tema))
