# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:31:41 2021

@author: T7097325

Estruturas Repetição For
"""

# Sintaxe Básica

"""
FOR
for elemento in sequencia:
    print(f'{elemento}')

RANGE
for (i = 0; i <= 10; i += 2)
range
"""

# sequencia = [1,2,3]

# for elemento in sequencia:
#     print(f'{elemento}')

for i in range(0, 10):
    print(f'Valor de i de 1 em 1 é: {i}')

print("")

for i in range(0, 10, 2):
    print(f'Valor de i de 2 em 2 é: {i}')

# Iterando sobre Estrutura de Dados
set_ = {1, 2, 3}
tupla = (1, 2, 3)
lista = [1, 2, 3]
dicionario = {'a': 1, 'b': 2, 'c': 3}

for elemento in set_:
    print(f'[SET] Elemento do set: {elemento}')

for elemento in tupla:
    print(f'[TUPLA] Elemento do tupla: {elemento}')

for elemento in lista:
    print(f'[LISTA] Elemento do lista: {elemento}')

for elemento in dicionario.items():
    print(f'[DICT] Elemento do dicionario: {elemento}')




