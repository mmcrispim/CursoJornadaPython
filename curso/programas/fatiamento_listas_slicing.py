# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:06:46 2021

@author: T7097325

Fatiamento de Listas (Slicing)

Sintaxe: lista[índice início: índice fim: passo]
o "passo" é de quanto em quanto os itens serão pegos na lista
o "índice fim" é excludente

"""

# letras = ['a','b','c','d','e','f']

# parte_1 = letras[0:3:1]
# parte_2 = letras[3:6:1]

# print(parte_1)
# print(parte_2)

# parte_2 = letras[::-1]

# print(parte_2)

# # Exemplos
#          0   1   2   3   4   5
letras = ['a','b','c','d','e','f']
#         -6  -5  -4  -3  -2  -1

parte_1 = letras[0:3:1]
parte_2 = letras[3:6:1]

# indexação positiva
print('indexação positiva')
print(parte_1)
print(parte_2)

print("")

# indexação negativa - invertendo
print('indexação negativa')
print(letras[-6:-3:1])
print(letras[-3:-1:1]) # o último elemento final não retornou
print(letras[-3::1]) # neste caso, não informar o último elemento e o Python entende que deve ir até o último elemento

print("")

print(letras[::-1])
print(letras[-1:-4:-1])
print(letras[-4:-7:-1])

print("")

print(letras[-3::1])
print(letras[::2])
print(letras[1::2])

# Operador "+" para concatenar listas
print(letras[::2] + letras[1::2])


