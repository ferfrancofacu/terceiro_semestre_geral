"""Escreva uma função contador que recebe uma string e devolve
um dicionário. A string só contém palavras em minúsculas,
separadas por espaços e sem pontuação. O dicionário indica
quantas ocorrências de cada palavra existem na string.
Por exemplo:

contador('esse exercício é um exercício fácil ou difícil')
Retorna:

{'é': 1, 'difícil': 1, 'esse': 1, 'ou': 1, 'um': 1, 'fácil': 1, 'exercício': 2}"""


def contador(palavras):
    lista_palavras = palavras.split(" ")

    dicionario = []

    for pl in dicionario:
        dicionario[pl] = lista_palavras.count(pl)  
    return dicionario
