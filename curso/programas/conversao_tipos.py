# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:27:39 2021

@author: T7097325

Conversão de Tipos
"""
idade = 35
texto = 'Parabéns João pelos seus ' + str(idade) + ' anos de idade!'
print(texto)

pontuacao_str = '10'
pontuacao_int = int(pontuacao_str)

print(f'Tipo: {type(pontuacao_str)}')
print(f'Tipo: {type(pontuacao_int)}')

pontuacao_str = '5.5'
pontuacao_float = float(pontuacao_str)

print(pontuacao_str)
print(pontuacao_float)

print(f'Tipo: {type(pontuacao_str)}')
print(f'Tipo: {type(pontuacao_float)}')
