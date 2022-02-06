# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:03:23 2021

@author: mmcri

ParÃ¢metros Posicionais
"""


# def funcao_com_args(arg1, arg2, *args):
#     print(f'Arg1: {arg1}')
#     print(f'Arg2: {arg2}')
#     print(f'*Arg: {args}')

# funcao_com_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def soma(*numeros):
#     resultado = 0
#     for numero in numeros:
#         resultado += numero

#     return resultado

# resultado_soma = soma(1, 2, 7)

# print(resultado_soma)

def soma_max(maximo, *numeros):
    resultado = 0
    numeros_somados = []

    for numero in numeros:
        if (resultado + numero) > maximo:
            break

        resultado += numero
        numeros_somados.append(numero)

    return resultado, numeros_somados


resultado_soma, numeros_somados = soma_max(100, 1, 2, 5, 10, 25, 35, 22)

print(f'Resultado {resultado_soma}')
print(f'NÃºmeros Somados {numeros_somados}')
