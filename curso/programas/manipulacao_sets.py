# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 15:31:39 2021

@author: T7097325

Manipulação de Sets
"""

# Criando Sets
lista = [1,2,3]
set_1 = {1,2,3,4,5,6}
set_2 = set(lista)

print("")

print(set_1)
print(type(set_1))

print("")

print(set_2)
print(type(set_2))

print("")

carteira = {'PETR4','CASH3','MGLU3','BBAS3','WEGE3'}
print(f'Carteira inicial: {carteira}')

# print("")

# Adicionando elementos com ADD
# carteira.add('ITSA4')
# print(f'Carteira após add(): {carteira}')

# print("")

# Atualizando elementos com UPDATE
# carteira.update({'PETR4','ABEV3','RAIZ4'})
# print(f'Carteira após update(): {carteira}')

# print("")

# Removendo elementos com DISCARD
# carteira.discard('PETR4')
# print(f'Carteira após discard: {carteira}')

# print("")

# Removendo elementos com REMOVE
# carteira.remove('ABEV3')
# print(f'Carteira após remove(): {carteira}')

# print("")

# Removendo elementos com POP (aleatório) - retira o último elemento
carteira.pop()
print(f'Carteira após pop(): {carteira}')

print("")

# Removendo elementos com CLEAR
carteira.clear()
print(f'Carteira após clear() {carteira}')
