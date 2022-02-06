# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:16:42 2021

@author: T7097325

f-Strings
"""

titulo = 'Monitor Gamer'
polegadas = 27
preco = 1299.99

print(f'Nome do Produto: {titulo} e Tamanho: {polegadas} polegadas.')

print(
      f'Produto: {titulo.upper()}\n'
      f'Tamanho: {polegadas}\n'
      f'Preço R$ {preco}'
      )

# Formatadores Especiais
"""
* é o caracter de preenchimento
^ é o caracter de posicionamento (no meio)
50 é o tamanho de preenchimento
ou seja, preencher com * colocando o título no meio e toda a string terá 50 caracteres
"""
print(
      f'Produto: {titulo.upper():*^50}\n'
      f'Tamanho: {polegadas}\n'
      f'Preço R$ {preco}'
      )

