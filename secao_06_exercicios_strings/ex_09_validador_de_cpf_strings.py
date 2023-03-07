"""
Exercício 09 da seção de strings da Python Brasil:
https://wiki.python.org.br/ExerciciosComStrings

Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
e indique se é um número válido ou inválido através da validação dos dígitos verificadores
e dos caracteres de formatação.

    >>> validar_cpf('734.289.251-30')
    True


    >>> validar_cpf('732.289.294-10')
    False


    >>> validar_cpf('44986045040')
    True


    >>> validar_cpf('6693171008')
    False


"""


def validar_cpf(cpf):
    """Escreva aqui em baixo a sua solução"""
    algarismos_cpf = list(map(int, cpf.replace('.', '').replace('-', '')))
    segundo_digito_verificador = algarismos_cpf.pop()

    soma_segunda_verificacao = sum(i * algarismo for i, algarismo in zip(range(11, 1, -1), algarismos_cpf))
    resto_por_11 = soma_segunda_verificacao % 11
    if resto_por_11 <= 1:
        calculo_segundo_digito_verificador = 0
    else:
        calculo_segundo_digito_verificador = 11 - resto_por_11
    if calculo_segundo_digito_verificador != segundo_digito_verificador:
        return False

    primeiro_digito_verificador = algarismos_cpf.pop()

    soma_primeira_verificacao = sum(i * algarismo for i, algarismo in zip(range(10, 1, -1), algarismos_cpf))
    resto_por_11 = soma_primeira_verificacao % 11
    if resto_por_11 <= 1:
        calculo_primeiro_digito_verificador = 0
    else:
        calculo_primeiro_digito_verificador = 11 - resto_por_11
    if calculo_primeiro_digito_verificador != primeiro_digito_verificador:
        return False

    return True
