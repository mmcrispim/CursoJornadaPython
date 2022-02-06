"""
Módulo Avançado
Map, Filter e as Funções Lambda
"""

# def trata_texto(texto):
#     return texto.replace("'","").strip()


cadastros = ["João, 18, joão@e'mail.com",
             "   Jo'ana, 22, joana@gmail.com    ",
             "Kléber, 30. kleber123@hotmai'l.com"
             ]

# resultado = []
#
# for cadastro in cadastros:
#     resultado.append(trata_texto(cadastro))
#
# print(resultado)

# resultado = list(map(trata_texto, cadastros))

resultado = list(map(lambda texto: texto.replace("'","").strip(), cadastros))

print(resultado)

resultado_filter = list(filter(lambda cadastro: 'gmail' in cadastro, resultado))

print(resultado_filter)