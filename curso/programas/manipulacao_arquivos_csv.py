# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 13:21:55 2021

@author: mmcri

Manipulação de Arquivos CSV
"""

"""
Objetivos:
    1. Ler arquivo de entrada CSV
    2. Processamento (Retirada do Campo ID e junção do campo NOME + SOBRENOME)
    3. Gravação do arquivo CSV de Saída
"""

resultados = []

# criando um gerenciador de contexto para a abertura do arquivo csv e desta forma não é necessário fechar o arquivo
with open("./dados/cadastro.csv", "r") as arquivo_entrada:
    linhas = arquivo_entrada.readlines()[1:]

    for linha in linhas:
        dados = linha.split(",")
        email = dados[3].replace('\n', '')
        resultados.append(f"{dados[1]} {dados[2]}, {email}\n")

    pass

# criando um gerenciador de contexto para gravação do arquivo de saída
with open("./dados/cadastro_saida.csv", "w") as arquivo_saida:
    for resultado in resultados:
        arquivo_saida.write(resultado)

