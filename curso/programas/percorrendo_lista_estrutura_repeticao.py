# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:21:03 2021

@author: T7097325

Percorrendo Listas com Estruturas de Repetição
"""

from random import randint

alunos = ['Mariangela', 'Raquel', 'Antonia', 'Chico', 'Bento']
notas = [randint(5, 10), randint(5, 10), randint(5, 10), randint(5, 10), randint(5, 10)]

# for aluno in alunos:
#     print(f'O nome do aluno é: {aluno}')

# for aluno in alunos:
#     nota = randint(2,10)
#     print(f'A nota do aluno {aluno} foi {nota}')

# for aluno in alunos:
#     nota_1 = randint(4,10)
#     nota_2 = randint(2,9)
#     nota_3 = randint(3,7)

#     nota_final = nota_1*0.2 + nota_2 * 0.3 + nota_3 * 0.5

#     print(f'A nota final do aluno {aluno} foi de {nota_final}')

# o zip vai iterar sobre as 2 listas ao mesmo tempo
# se uma das listas tiver tamanho menor que a outra lista, o zip vai parar no
# menor índice
for aluno, nota in zip(alunos, notas):
    print(f'A nota do aluno {aluno} foi {nota}')



