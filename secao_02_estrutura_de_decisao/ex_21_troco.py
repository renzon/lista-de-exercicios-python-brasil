"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    tipos_de_notas = [1, 5, 10, 50, 100]
    pedacos = []
    resto = valor
    while resto > 0:
        tipo_de_nota = tipos_de_notas.pop()
        quantidade, resto = divmod(resto, tipo_de_nota)
        if quantidade == 0:
            continue
        elif quantidade == 1:
            pedaco = f'{quantidade} nota de R$ {tipo_de_nota}'
        else:
            pedaco = f'{quantidade} notas de R$ {tipo_de_nota}'
        pedacos.append(pedaco)

    ultimo_pedaco = pedacos.pop()
    if len(pedacos) == 0:
        return ultimo_pedaco

    pedacos_separados_por_virgula = ', '.join(pedacos)
    return f'{pedacos_separados_por_virgula} e {ultimo_pedaco}'
