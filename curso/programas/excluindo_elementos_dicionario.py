# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:35:56 2021

@author: T7097325

Excluindo elementos de Dicionários
"""

fila = {
    '0':'Raquel',
    '1':'Mariângela',
    '2':'Antonia',
    '3':'Chico',
    '4':'Bento',
    '5':'Saci',
    '6':'Diabo da Tasmânia'
    }

print(f'Fila Inicial: {fila}')

print("")

# Primeira forma de exclusão: del
del fila['0']

print(f'Fila atualizada: {fila}')

print("")

# Segunda forma de exclusão: pop

valor_retirado = fila.pop('1')

print(valor_retirado)
print(f'Fila atualizada: {fila}')

print("")

# Terceira forma de exclusão: popitem

valor_retirado = fila.popitem()

print(valor_retirado)
print(f'Fila atualizada: {fila}')

print("")

# Quarta forma de exclusão: clear

fila.clear()
print(fila)


