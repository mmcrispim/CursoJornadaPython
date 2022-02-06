# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:22:09 2021

@author: mmcri

Manipulação de Arquivos com a Função Open
"""

# MODO DE ABERTURA DE ARQUIVOS
# ------------------------------------------------
#                    |  TEXTO  |   BINÁRIO
# ------------------------------------------------
# Leitura            |   "r"   |    "rb"
# Leitura/ Escrita   |   "r+"  |    "rb+"
# ------------------------------------------------
# Escrita            |   "w"   |    "wb"
# Escrita / Leitura  |   "w+"  |    "wb+"
# ------------------------------------------------
# Anexar             |   "a"   |    "ab"
# Anexar / Leitura   |   "a+"  |    "ab+"
# ------------------------------------------------

# texto = "\n\nVenha DOMINAR Python!"

# arquivo = open("Z:\\Wrk_Cursos\\DataScienceAcademy\\Python\\JornadaPython\\dados\\dados.txt","w")

# arquivo = open("Z:\\Wrk_Cursos\\DataScienceAcademy\\Python\\JornadaPython\\dados\\dados.txt","r")

# arquivo = open("Z:\\Wrk_Cursos\\DataScienceAcademy\\Python\\JornadaPython\\dados\\dados.txt","a")

# arquivo.write(texto)

# # print(retorno)

# arquivo.close()

arquivo_png = open("Z:\\Wrk_Cursos\DataScienceAcademy\Python\JornadaPython\imagens\\images.png","rb")

retorno_png = arquivo_png.read()

arquivo_saida = open("Z:\\Wrk_Cursos\DataScienceAcademy\Python\JornadaPython\imagens\\images_saida.png","wb")

arquivo_saida.write(retorno_png)

# print(retorno_png)

arquivo_png.close()
arquivo_saida.close()


