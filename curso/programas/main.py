# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 17:31:35 2021

@author: mmcri

main
"""

# import matematica

# print(matematica.soma(1, 2))

# print(matematica.subtracai(5, 3))

# ===============================================================================================

# from matematica import soma, subtracao # pode tirar soma e subtracao e colocar * para puxar todas as funÃ§Ãµes *** CUIDADO! ***

# print(subtracao(10, 7))

# print(soma(5, 3))

# ===============================================================================================

from operacoes.soma import soma_dois_numeros
from operacoes.subtrai import subtrai_dois_numeros

print(soma_dois_numeros(7, 13))

print("")

print(subtrai_dois_numeros(12, 4))






