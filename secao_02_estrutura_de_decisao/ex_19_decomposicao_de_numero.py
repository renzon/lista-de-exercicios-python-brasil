"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

"""


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""
    if numero >= 1000:
        return 'O número precisa ser menor que 1000'

    if numero <= 0:
        return 'O número precisa ser positivo'

    pedacos = []

    centena, resto = divmod(numero, 100)
    if centena == 1:
        pedacos.append('1 centena')
    elif centena > 0:
        pedacos.append(f'{centena} centenas')

    dezena, resto = divmod(resto, 10)
    if dezena == 1:
        pedacos.append('1 dezena')
    elif dezena > 0:
        pedacos.append(f'{dezena} dezenas')

    unidade = resto
    if unidade == 1:
        pedacos.append('1 unidade')
    elif unidade > 0:
        pedacos.append(f'{unidade} unidades')

    if len(pedacos) == 1:
        decomposicao = pedacos.pop()
    elif len(pedacos) == 2:
        primera_parte, segunda_parte = pedacos
        decomposicao = f'{primera_parte} e {segunda_parte}'
    else:
        primera_parte, segunda_parte, terceira_parte = pedacos
        decomposicao = f'{primera_parte}, {segunda_parte} e {terceira_parte}'

    return f'{numero} = {decomposicao}'
