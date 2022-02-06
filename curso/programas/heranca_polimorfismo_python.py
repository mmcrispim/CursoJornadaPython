# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:41:09 2022

@author: mmcri
Herança e Polimorfismo no Python
"""

VALOR_PEDAGIO_CARRO = 3.5
VALOR_PEDAGIO_MOTO = 2.75
VALOR_KM_RODADO_CARRO = 1.5
VALOR_KM_RODADO_MOTO = 1.0


class Automovel:
    # método construtor
    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente = ""

        print(f"Automóvel {self.montadora} {self.modelo} adquirido pela Locadora!")

    def alugar(self, nome_cliente):
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f'O Automóvel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}!')

    def devolver_automovel(self):
        self.alugado = False
        print(f'O Automóvel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}!')
        # self.nome_cliente = ""

    def gerar_valor_fatura(self, numero_pedagios, quilometros_rodados):
        raise NotImplementedError


class Carro(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado)
        print("O Automóvel adquirido foi um Carro!")

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_CARRO + km_rodados * VALOR_KM_RODADO_CARRO
        print(
            f'Fatura do carro {self.montadora} {self.modelo} gerada com sucesso no valor de R$ {self.valor_fatura:.2f}')


class Moto(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado)
        print("O Automóvel adquirido foi uma Moto!")

    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_MOTO + km_rodados * VALOR_KM_RODADO_MOTO
        print(
            f'Fatura da moto {self.montadora} {self.modelo} gerada com sucesso no valor de R$ {self.valor_fatura:.2f}')


def mostrar_fatura(automovel):
    print(
        f"O valor da Fatura do Automóvel {automovel.montadora} {automovel.modelo} alugado por {automovel.nome_cliente} "
        f"ficou no valor de R$ {automovel.valor_fatura:.2f}")


# ============================================================================================================== #

fiesta = Carro("Ford", "Fiesta", False)
fiesta.alugar("Mariângela")

# Simulação do tempo de aluguel
from time import sleep
from random import randint

sleep(randint(7, 10))

fiesta.devolver_automovel()

fiesta.gerar_valor_fatura(5, 750)

mostrar_fatura(fiesta)

print("")

honda_cb = Carro("Honda", "CB500", False)
honda_cb.alugar("Raquel")

sleep(randint(7, 10))

honda_cb.devolver_automovel()

honda_cb.gerar_valor_fatura(3, 500)

mostrar_fatura(honda_cb)