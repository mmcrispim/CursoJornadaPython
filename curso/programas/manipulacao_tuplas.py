# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:26:49 2021

@author: T7097325

Manipulação de Tuplas
"""

# Criação de Tuplas

# lista = [5,6,7]
# tupla = (1,2,3)
# tupla2 = tuple(lista)
# print(type(tupla))
# print(tupla)
# print(tupla2)

# tupla = (1,)
# print(type(tupla))

tupla = 1,2,3,4,5,6,7,8,9,10
print(tupla)

print("")

# Indexação
print(f'O quinto elemento da Tupla é: {tupla[4]}')

print("")

# Indexação Negativa
print(f'O último elemento da Tupla é: {tupla[-1]}')

print("")

# Slicing
tupla_slicing = tupla[4:]
print(tupla_slicing)

print("")

# Tentativa de alteração de valores
# tupla[0] = 1
# print(tupla)

print("")

# Deleção com del
# del tupla[0]
# del tupla

# Métodos
print(f'A quantidade de elementos iguais a 1 é {tupla.count(1)}')
print(f'O elemento 10 está na posição: {tupla.index(10)}')

# Iteração
for elemento in tupla:
    print(f'Elemento = {elemento}')