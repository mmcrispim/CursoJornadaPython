# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:41:10 2021

@author: mmcri

Tratamento de Erros com Try/Except
"""

"""
try:
    # Código a ser testado

except:
    # Execute este código caso algum erro ocorra

else:
    # Execute este código caso nenhum erro ocorra

finally:
    # Sempre execute este código

"""


def divide_dois_numeros(dividendo, divisor):
    return dividendo / divisor


try:
    # Código a ser testado
    numero_1 = int(input("Digite o primeiro número: "))
    numero_2 = int(input("Digite o segundo número: "))

    resultado = divide_dois_numeros(numero_1, numero_2)

# except TypeError:
#     print("Erro de Tipos")

# except ZeroDivisionError:
#     print("Divisão por zero não suportada.")

except (ZeroDivisionError, TypeError) as excecao:
    print(f"Divisão por zero não suportada ou Erro de Tipagem. Erro {excecao}")

except Exception:
    # Execute este código caso algum erro ocorra
    print("Um erro ocorreu!")

else:
    # Execute este código caso nenhum erro ocorra
    print(f'O Resultado da Divisão é {resultado}')

finally:
    # Sempre execute este código
    print("Finalizando o programa... Muito obrigada!")


