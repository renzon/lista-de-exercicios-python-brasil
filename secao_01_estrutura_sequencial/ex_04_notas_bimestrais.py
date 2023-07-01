"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media()
    A média anual é 8.5

"""


def calcular_media():
    """Escreva aqui em baixo a sua solução"""
    notas_bimestrais = 0
    for i in range(4):
        i = float(input(f'Insira a nota do {i+1} bimestre: '))
        notas_bimestrais+=i
    media_bimestre = notas_bimestrais / 4

    print(f'A média anual é {media_bimestre}')

