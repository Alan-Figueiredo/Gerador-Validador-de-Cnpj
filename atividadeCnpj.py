
# from random import randint
# numero = str(randint(100000000000,999999999999))

import re

dig1 = 0
dig2 = 0


def valida(cnpj):
    cnpj = apenas_numeros(cnpj)
    return cnpj
    
def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]','',cnpj)
    
def sequencia(sequencia,cnpj):
    global mult
    sequence1,sequence2 = [a for a in range(sequencia,1,-1)],[a for a in range(9,1,-1)]
    sequence_uniao = sequence1 + sequence2
    mult = [int(x) * y for x,y in zip(cnpj,sequence_uniao)]

    return mult

def calculo(digito):

    conta = 11 - (soma % 11)
    if conta > 9:
        digito = 0
    else:
        digito = conta

    return str(digito)

cnpj = valida('31.662.305/3977-31')

soma = sum(sequencia(5,cnpj[:-2]))

part1 = cnpj[:-2] + calculo(dig1)

soma = sum(sequencia(6,part1))

new_cnpj = part1 + calculo(dig2)

print((f'{new_cnpj[:2]}.{new_cnpj[2:5]}.{new_cnpj[5:8]}/{new_cnpj[8:12]}-{new_cnpj[12:14]}'))

if cnpj == new_cnpj:
    print('Cnpj Valido')
else:
    print('Cpnj Invalido')
