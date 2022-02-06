# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:45:43 2021

@author: T7097325

Estrutura de Repetição While
"""

# IMPORTS
from random import randint

# VARIAVEIS
capacidade_maxima_balde = 1000 # 1000 ml
balde = 0 # valor atual do balde

# PROCESSO
while balde <= capacidade_maxima_balde:
    volume_copo = randint(95, 100)
    print(f'O copo foi enchido com {volume_copo} mls')
    balde += volume_copo
    print(f'O Volume do Balde é de {balde} mls\n')

print(f'O Volume do Balde ultrapassou a capacidade máximade {capacidade_maxima_balde} mls e esta com {balde}mls')
