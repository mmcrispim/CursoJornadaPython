# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:50:12 2021

@author: T7097325

Strings
"""
nome = 'Bento'
sobrenome = 'Gael Pipoca'
nome_completo = nome + " " + sobrenome

print(nome + " " + sobrenome)
print(nome_completo)
print(nome_completo.lower())

nome = '   Chico'
sobrenome = '    Snow Pipoca'
nome_completo = nome.strip() + " " + sobrenome.strip()

print(nome_completo)

# \n = new line - quebra a linha no ponto onde for colocado
print(nome_completo + ' é um dos meus gatos. \no outro é o Bento')

# \t = tabulação => tecla tab
print('\t' + nome_completo + ' é um dos meus gatos. \no outro é o Bento')

# \' = permite colocar uma aspas simples no meio da string sem que o código
# identifique fim da string
print('\t' + nome_completo + 'é um dos meus gatos. \no outro é o Bento e ele é \'LINDO\'')

# Outra forma de criar string
mes = str('Janeiro')
print(mes)
