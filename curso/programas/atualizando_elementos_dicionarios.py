# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:24:55 2021

@author: T7097325

Adicionando e Atualizando elementos em DicionÃ¡rios
"""
computador = {
    'cpu':'Core i7',
    'ram':'DDR4 16Gb',
    'ssd':'Samsung Evo 840 256Gb',
    'gpu':'RTX 2080 Ti'
    }

print(f'Computador v1: {computador}')

print("")

computador['ram'] = 'DDR4 32Gb'

print(f'Computador v2: {computador}')

print("")

computador['fonte'] = 'Fonte 600W Corsair'

print(f'Computador v3: {computador}')

print("")

computador.update({'fonte':'Corsair 850W'})

print(f'Computador v4: {computador}')

print("")

computador.update({'fonte':'Corsair 850W','ssd':'Samsung Evo 840 1Tb'})

print(f'Computador v5: {computador}')





