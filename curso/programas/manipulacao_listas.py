# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:29:03 2021

@author: T7097325

Manipulação de Listas
"""
sacola = ['Arroz','Feijão','Carne','Farinha']

print(f'A lista inicial é: {sacola}')

print("")
# MÉTODO: APPEND(objeto)
# Adiciona um item ao fim da lista

sacola.append('Leite')
print(f'Lista após a chamada do método APPEND(): {sacola}')

print("")
# MÉTODO: EXTEND(estrutura)
# Adiciona todos os itens de outra estrutura ao fim da lista

sacola.extend(['Sal','Macarrão','Maionese'])
print(f'Lista após a chamada do método EXTEND(): {sacola}')

print("")
# MÉTODO: INSERT(índice, objeto)
# Insere um item na posição desejada

sacola.insert(0,'Café')
print(f'Lista após a chamada do método INSERT(): {sacola}')

print("")
# MÉTODO: REMOVE(objeto)
# Remove o primeiro elemento igual ao valor passado

sacola.remove('Maionese')
print(f'Lista após a chamada do método REMOVE(): {sacola}')

print("")
# MÉTODO: POP(índice)
# Remove o item da posição desejada da lista e o retorna
# Caso o índice não seja especificado, retorna o último elemento

sacola.pop()
elemento = sacola.pop(3)
print(f'Lista após a chamada do método POP(): {sacola}')
print(elemento)

print("")
# MÉTODO: CLEAR(objeto)
# Remove todos os elementos da lista

sacola.clear()
print(f'Lista após a chamada do método CLEAR(): {sacola}')

sacola = ['Arroz','Feijão','Carne','Farinha']

print("")
# MÉTODO: INDEX(valor[,começo, fim])
# Retorna o índice do primeiro elemento do valor especificado
# Podemos ainda passar outros 2 parâmetros que dizem onde pesquisar na lista (começo e fim)

sacola.index('Farinha',0,4)
# print(sacola.index('Arroz'))
print(f'Lista após a chamada do método INDEX(): {sacola}')

print("")
# MÉTODO: COUNT(valor)
# Conta o número de ocorrências do valor especificado na lista

sacola.count('Arroz')
print(f"Lista após a chamada do método COUNT(): {sacola.count('Arroz')}")

print("")
# MÉTODO: SORT([chave, reverso])
# Ordena os itens da lista. Parâmetros adicionais podem ser utilizados para customizar a ordenação

sacola.sort()
print(f'Lista após a chamada do método SORT(): {sacola}')
sacola.sort(reverse=True)
print(f'Lista após a chamada do método SORT(): {sacola}')

print("")
# MÉTODO: REVERSE(valor)
# Reverte os elementos da lista

sacola = ['Arroz','Feijão','Carne','Farinha']

sacola.reverse()
print(f"Lista após a chamada do método REVERSE(): {sacola}")

print("")
# MÉTODO: COPY()
# Retorna uma lista com a cópia dos elementos da lista de origem

copia_sacola = sacola.copy()
print(f"Lista após a chamada do método COPY(): {copia_sacola}")


