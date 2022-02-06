# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:24:45 2021

@author: mmcri

Principais Erros e Exceções:
    - ZeroDivisionError: division by zero
    - NameError: name 'divisoir' is not defined
    - TypeError: unsupported operand type(s) for /: 'str' and 'int'
    - IndentationError: expected an indented block
"""

def divide_dois_numeros(dividendo, divisor):
    return dividendo / divisor

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

resultado = divide_dois_numeros(numero_1, numero_2)

print(f'O Resultado da Divisão é {resultado}')
