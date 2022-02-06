# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:04:47 2021

@author: T7097325

Método Format
"""
nome = 'João'
sobrenome = 'Oliveira'
idade = 32

print('Meu nome é {} {} e tenho {} anos'.format(nome, sobrenome, idade))

print('Meu nome é {nome} {sobrenome} e tenho {idade} anos'.format(nome=nome, sobrenome=sobrenome, idade=idade))

valor = 547.58

# utilizando apenas 1 casa decimal e a variável é do tipo float
print('O valor é R$ {valor:.1f}'.format(valor=valor))


