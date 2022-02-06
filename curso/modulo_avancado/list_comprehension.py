"""
Módulo Avançado
Compreensão de Listas (List Comprehensions)
"""

emails = [
    ',henRy@gmail.com',
    ' ,juLIa@hotmail.com  ',
    'ivaN@gmail.com ',
    'mar,coS@yahoo.com.br   ',
    '   SandoVAl@hotmail.com',
    'IVANA@gmail.com',
    'ItamaR@edu.gov.br'
]

emails_tratatos = [email.strip().replace(",","").lower() for email in emails]

emails_tratatos_gmail = [email.strip().replace(",","").lower() for email in emails if '@gmail' in email]

print(emails_tratatos)

print(emails_tratatos_gmail)

# Múltiplos comuns de 4 e 5 de 0 a 500

resultado = [numero for numero in range(0, 501) if numero % 4 == 0 if numero % 5 == 0]

print(resultado)