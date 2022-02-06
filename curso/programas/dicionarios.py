# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 10:09:23 2021

@author: T7097325

Dicionários
"""
# Criando um dicionário
cadastro = {
    'id':1,
    'nome':'Mariângela Crispim',
    'filhos':['Chico','Bento'],
    'compras':[
        {
            'id':4578,
            'produto':'Notebook Gamer',
            'preco':2597.99
            }
        ]
    }

print(cadastro)

print("")

# Acessando os dados do dicionário
# print(cadastro['id'])
# print(cadastro['nome'])
# print(cadastro['compras'][0])
# print(type(cadastro['compras']))
# print(f"O usuário {cadastro['nome']} realizou a seguinte compra {cadastro['compras'][0]['produto']}")

usuario = cadastro['nome']
produto = cadastro['compras'][0]

print(f"O usuário {usuario} realizou a seguinte compra: {produto['produto']}")

# Usando o método get()
# esta função tem um valor default para o caso de não existir a informação.
filhos = cadastro.get("filhos", None)
print(filhos)

altura = cadastro.get("altura", None)
print(altura)



