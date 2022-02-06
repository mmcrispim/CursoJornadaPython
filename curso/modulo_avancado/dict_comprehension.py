"""
Módulo Avançado
Compreensão de Dicionários (Dict Comprehensions)
"""

# clientes = {
#     'Maria': '041.587.565-85',
#     'Jonas': '140.857.965-16',
#     'Carlos': '136.857.963-88',
#     'Marcos': '745.878.969-12'
# }

# resultado = {}
#
# for chave, valor in clientes.items():
#     resultado[chave] = valor.replace("-","").replace(".","")
#
# print(resultado)

# Forma básica: {chave, valor for item in sequencia}

# resultado = {chave.upper(): valor.replace("-","").replace(".","") for chave, valor in clientes.items()}
#
# print(resultado)

cadastro = {
    'Maria': 4500,
    'Marcos': 7800,
    'Gabriel': 3750,
    'João': 15000
}

salario_maior_5000 = {chave:valor for chave,valor in cadastro.items() if valor > 5000}

print(salario_maior_5000)