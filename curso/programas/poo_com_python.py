# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 17:00:23 2022

@author: mmcri

Programação Orientada a Objetos no Python
"""


# Classe Celular?
#   Atributos:
#       Fabricante: String
#       Modelo: String
#       Tela: Decimal
#       Armazenaento: Inteiro
#       Memória: Inteiro
#       CAmera: Inteiro
#       Bateria: Inteiro
#       Tela Ligada: Booleano
#   Métodos:
#       ligar_tela()
#       salvar_em_disco()
#       carregar_aplicativo()
#       tirar_foto()
#       verificar_carga_bateria()

# nome seguindo regra CamelCase (primeira letra de cada palavra em maiúsculo e sem underline)
class Celular:
    # método construtor: método chamado toda vez que objetos estiverem instanciando essa classe e é neste método que se
    # faz a definição dos atributos da classe
    def __init__(self, fabricante, modelo, tela, armazenamento, memoria, camera, bateria, tela_ligada):
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = armazenamento
        self.memoria = memoria
        self.camera = camera
        self.bateria = bateria
        self.tela_ligada = tela_ligada

    def ligar_tela(self):
        self.tela_ligada = True

    def verificar_carga_bateria(self):
        # Utilizar a função random do módulo random
        # Printe na tela uma porcentagem e o valor correspondente em mA
        # Exemplo: "O Celular esta com 46% de Bateria e 1564mA restantes"
        pass


# instanciar a classe
# passagem de parâmetros posicional
celular_android = Celular("Samsung", "S10", 6.25, 128, 4, 21, 3400, False)

# passagem de parâmetros não posicional
celular_iphone = Celular(fabricante="Apple",
                         modelo="iPhone 13 Pro",
                         tela=5.75,
                         armazenamento=128,
                         memoria=4,
                         camera=21,
                         bateria=3400,
                         tela_ligada=False)

celular_iphone.ligar_tela()

print(celular_iphone.tela_ligada)




