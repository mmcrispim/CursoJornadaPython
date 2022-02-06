# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:01:19 2021

@author: mmcri

Calculadora utilizando Funções
"""


def soma(numeros):
    return int(numeros[0]) + int(numeros[1])


def divisao(numeros):
    return int(numeros[0]) / int(numeros[1])


def multiplicacao(numeros):
    return int(numeros[0]) * int(numeros[1])


def subtracao(numeros):
    return int(numeros[0]) - int(numeros[1])


numeros_input = input('Digite os números separados por espaço:').split(' ')
operacao_input = input('Digite a operação (+ / * 0): ')
resultado_calculado = 0

if len(numeros_input) != 2:
    print('Quantidade de entradas diferente de 2')
else:
    if operacao_input in '+/*-':
        if operacao_input == '+':
            resultado_calculado = soma(numeros_input)

        elif operacao_input == '/':
            resultado_calculado = divisao(numeros_input)

        elif operacao_input == '*':
            resultado_calculado = multiplicacao(numeros_input)

        elif operacao_input == '-':
            resultado_calculado = subtracao(numeros_input)

        print(f'Resultado Calculado: {resultado_calculado}')

    else:
        print(f'Operação {operacao_input} Inválida')


