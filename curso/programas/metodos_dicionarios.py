# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:49:59 2021

@author: T7097325

Métodos de Dicionários
"""

familia = {
    'pai':'José Crispim de Araújo',
    'mãe':'Antonia Arantes de Medeiros Araújo',
    'filho':'José Crispim de Araújo Junior',
    'filha':'Rosângela Medeiros Crispim Araújo'
    }

print(f'Familia: {familia}')

print("")

# Método COPY() - copia um dicionario
copia_familia = familia.copy()

print(f'Cópia do Dicionário Familia {copia_familia}')

print("")

# Método ITEMS() - Retorna os pares chave:valor em formato de lista
itens = familia.items()

print(f'Itens {itens}')

for item in itens:
    print(f'\tChave = {item[0]} e Valor = {item[1]}')

print("")

# Método KEYS() - Retorna todas as chaves em formato de lista
chaves = familia.keys()

print(f'Chaves {chaves}')

for chave in chaves:
    print(f'\tChave: {chave}')

print("")

# Método VALUES() - Retorna todos os valores em forma de lista
valores = familia.values()

print(f'Valores: {valores}')

for valor in valores:
    print(f'\tValor: {valor}')

print("")

# Método SETDEFAULT() - Insere a chave com o valor passado SE a chave
#                       não estiver presente no dicionário.
#                       Retorna o valor da chave SE a chave já estiver
#                       presente no dicionário
familia.setdefault('sobrinho','Huguinho')

print(f'Familia: {familia}')

mae = familia.setdefault('mãe','Dona Florinda')

print(f'Familia: {familia}')
print(mae)

print("")

# Método FROMKEYS - Cria um dicionário a partir de uma lista de chaves e um valor
chaves = ['mãe','pai','filho','filha']
valor = 0

jogo = dict.fromkeys(chaves, valor)

print(f'Jogo: {jogo}')