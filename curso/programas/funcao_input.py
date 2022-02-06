# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:44:59 2021

@author: T7097325

Função Input
"""
# nome = input('Qual o seu nome?')

# print(nome)

# idade = input('Qual a sua idade?')

# print(idade)

# Entrada
# numero = input('Digite o número desejado:')
# expoente = input('Digite o expoente:')

# Processamento
# resultado = int(numero) ** int(expoente)

# Saída
# print(f'O resultado de {numero} elevado à {expoente} é {resultado}')

nome = input('Qual o seu nome?')
idade = input('Qual a sua idade?')
altura = input('Qual a sua altura')

print('Os dados inseridos foram:')
print(
      f'\tNome: {nome}\n'
      f'\tIdade: {idade} anos\n'
      f'\tAltura: {float(altura):.2f}')