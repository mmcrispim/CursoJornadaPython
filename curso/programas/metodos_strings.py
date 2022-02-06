# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:26:04 2021

@author: T7097325

Métodos Strings
"""
print('     Strip     ')
print('     Strip     '.strip())

print('maiúsculo'.upper())
print('MAIÚSCULO'.lower())
print('T,exto, c,o,m vá,ri,as v,ír,gu,las'.replace(',',''))
print('Texto teste para função count'.count('e'))
print('Texto Centralizado'.center(50,'*'))
print('Avião?'.index('ã'))
print('Alfanumérico'.isnumeric())
print('Teste de quebra de string com split'.split(' '))
print('NOME;CIDADE;IDADE;PAIS'.split(';'))
print('este é um título'.title())
print('este é um título'.capitalize())
print('585'.zfill(5))

# Encadeamento de Funções
print('    Te;x;;to          '.strip().replace(';','').center(25,'*').upper())

# Tamanho de Strings
string_extensa = 'Essa é uma string extensa. Como faremos ' \
                 'para saber seu tamanho?'
print(len(string_extensa))
