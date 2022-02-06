# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 15:50:17 2021

@author: T7097325

Operações Matemáticas em Sets
"""

homens = {'João','Joaquim','Alberto','Antônio','Leonardo','Victor','Kléber','Marcelo','Alfredo'}
alta_renda = {'Ana','Joaquim','Joana','Antônio','Kléber','Marcelo','Alfredo','Carla','Adriana'}

print(f'Conjunto de Homens: \t{homens}')
print("")
print(f'Conjunto de Alta Renda: {alta_renda}\n{"-" * 150}\n')

print("")
# Interseção: Itens que estão em ambos os conjuntos
homens_alta_renda = homens.intersection(alta_renda)

print(f'Usuários Homens com Alta Renda: {homens_alta_renda}')

print("")
# União: Itens de ambos os conjuntos
homens_e_alta_renda = homens.union(alta_renda)

print(f'Homens e Usuários com Alta Renda: {homens_e_alta_renda}')

print("")
# Diferença: Itens que estão apenas em um dos conjuntos
homens_nao_alta_renda = homens.difference(alta_renda)
alta_renda_nao_homens = alta_renda.difference(homens)

print(f'Usuários Homens não Alta Renda: {homens_nao_alta_renda}')
print(f'Usuários Alta Renda não Homens: {alta_renda_nao_homens}')

print("")
# Diferença Simétrica: Itens que estão em um conjunto ou em outro mas não em ambos
homens_nao_alta_renda_e_mulheres = homens.symmetric_difference(alta_renda)

print(f'Usuários Homens não Alta Renda e Usuários Mulheres Alta Renda: {homens_nao_alta_renda_e_mulheres}')

print("")
# Métodos de Conjuntos
print(f'Os conjuntos de Homens e Alta Renda são disjuntos? {homens.isdisjoint(alta_renda)}')
print(f'O conjunto de Homens é um subconjunto de Alta Renda? {homens.issubset(alta_renda)}')
print(f'O conjunto de Homens é um superconjunto de Alta Renda? {homens.issuperset(alta_renda)}')

print("")

# Interseção:
print(f'Interseção {homens & alta_renda}')

# União:
print(f'União {homens | alta_renda}')

# Diferença:
print(f'Diferença {homens - alta_renda}')




