# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 11:19:08 2021

@author: T7097325

Estruturas Condicionais

Concedendo Aposentadoria
"""

# Entradas
idade = input('Digite a sua idade:')
sexo = input('Digite o seu sexo ("M" para Masculino e "F" para Feminino):')

if sexo.upper() == 'M':
    # Código para o Sexo Masculino
    if int(idade) >= 65:
        print("Parabéns, sua Aposentadoria será concedida!")

    else:
        print(f'Sua vez ainda não chegou! Aguarde mais {65 - int(idade)} anos.')

elif sexo.upper() == "F":
    # Código para o Sexo Feminino
    if int(idade) >= 60:
        print("Parabéns, sua Aposentadoria será concedida!")

    else:
        print(f'Sua vez ainda não chegou! Aguarde mais {60 - int(idade)} anos.')

else:
    print("Opção Inválida! Favor tentar novamente.")

