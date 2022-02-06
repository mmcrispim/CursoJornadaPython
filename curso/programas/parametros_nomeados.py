# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:20:27 2021

@author: mmcri

Parâmetros Nomeados
"""


def monta_computador(cpu, memoria, hd, *precos, monitor=17, **outros_atributos):
    print('O computador montado foi: ')
    print(f'\tCPU: {cpu}')
    print(f'\tMemória: {memoria}Gb')
    print(f'\tHD: {hd}Tb')
    print(f'\tPreços Praticados:')

    for preco in precos:
        print(f'\t\t R${preco:.2f}')

    print(f'\tMonitor: {monitor} polegadas')
    print('\tOutros Atributos')

    for chave, valor in outros_atributos.items():
        print(f'\t\t {chave}: {valor}')


monta_computador('Core i7', 16, 2, 2500, 3199, 4200, monitor=25, webcam='Webcan Multilaser',
                 teclado='Teclado Multilaser')