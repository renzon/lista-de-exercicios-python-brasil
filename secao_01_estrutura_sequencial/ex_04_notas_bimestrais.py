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

    nota_primero_bimestre = float(input('Digite a nota do 1º bimestre: '))
    nota_segundo_bimestre = float(input('Digite a nota do 2º bimestre: '))
    nota_terceiro_bimestre = float(input('Digite a nota do 3º bimestre: '))
    nota_quarto_bimestre = float(input('Digite a nota do 4º bimestre: '))

    soma_das_notas = nota_primero_bimestre + nota_segundo_bimestre + nota_terceiro_bimestre + nota_quarto_bimestre

    media = soma_das_notas / 4
    print(f'A média anual é {media}')