# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:58:00 2021

@author: T7097325

Construindo uma calculadora
"""
numero_1 = input('Digite o primeiro número: ')
numero_2 = input('Digite o segundo número: ')

print('Digite a operação:\n\t+ para Adição\n\t- para Subtração\n\t* para Multiplicação\n\t/ para Divisão')

operacao = input('Digite a operação: ')

equacao = f'{numero_1} {operacao} {numero_2}'

resultado = eval(equacao)

print(f'{"*" * 25}Resultado: {resultado}\n{"*" * 25}')

