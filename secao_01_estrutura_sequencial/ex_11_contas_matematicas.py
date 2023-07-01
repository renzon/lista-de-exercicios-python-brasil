"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 1) o produto do dobro do primeiro com metade do segundo;
 2) a soma do triplo do primeiro com o terceiro;
 3) o terceiro elevado ao cubo.

 Apresente os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_11_contas_matematicas
    >>> numeros = ['3.14', '43', '42']
    >>> ex_11_contas_matematicas.input = lambda k: numeros.pop()
    >>> ex_11_contas_matematicas.calcular_formulas()
    O produto do dobro do primeiro com metade do segundo é 1806.00
    A soma do triplo do primeiro com o terceiro é 129.14
    O terceiro elevado ao cubo é 30.96

"""


def calcular_formulas():
    """Escreva aqui em baixo a sua solução"""
    num_int1 = int(input('Informe com o primeiro numero inteiro: '))
    num_int2 = int(input('Informe com o segundo numero inteiro: '))
    num_real = float(input('Informe um número real: '))

    calc1 = ((num_int1 * 2) * (num_int2/2))
    calc2 = ((num_int1 * 3) + num_real)
    calc3 = (num_real **3)
    
    print(f'O produto do dobro do primeiro com metade do segundo é {calc1:.2f}')
    print(f'A soma do triplo do primeiro com o terceiro é {calc2:.2f}')
    print(f'O terceiro elevado ao cubo é {calc3:.2f}')

