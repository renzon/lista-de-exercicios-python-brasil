"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
Arredonde o tempo em minutos

    >>> from secao_01_estrutura_sequencial import ex_18_tempo_de_download
    >>> numeros =['50', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 7 minuto(s)
    >>> numeros =['100', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 3 minuto(s)

"""


def calcular_tempo_de_download():
    """Escreva aqui em baixo a sua solução"""
    tamanho = float(input('Informe o tamanho do arquivo (em MB): '))
    velocidade = float(input('Informe a velocidade de conexao (em Mbps): '))

    tamanho_em_bits = tamanho * 1024 * 1024 * 8
    tamanho_em_segundos = tamanho_em_bits / (velocidade * 1024 * 1024)
    tempo_em_minutos = tamanho_em_segundos / 60

    print(f'O tempo aproximado do Download é: {round(tempo_em_minutos)} minuto(s)')
