
def ohmTensao (r,i):
    tensao = r * i
    return tensao

def ohmCorrente (v,r):
    corrente = v / r
    return corrente

def ohmResistencia (v,i):
    resistencia = v / i
    return resistencia

print ('Deseja calcular qual grandeza? ')
print ('[1] Tensão')
print ('[2] Corrente')
print ('[3] Resistência')
z = str(input('Qual a sua opção? : '))

if z == '1':
    cor = float(input('Digite a corrente : '))
    res = float(input('Digite a resistência: '))
    v1 = ohmTensao (res,cor)
    print('A tensão para esta corrente e esta resistência é de {} Volts'.format(v1))

elif z == '2':
    ten = float(input('Digite a tensão : '))
    res = float(input('Digite a resistência: '))
    c1 = ohmCorrente (ten,res)
    print('A corrente para esta tensão e esta resistência é de {} Amperes'.format(c1))

elif z == '3':
    ten = float(input('Digite a tensão : '))
    cor = float(input('Digite a corrente : '))
    r1 = ohmResistencia (ten,cor)
    print('A resistência para esta tensão e esta corrente é de {} Ohms'.format(r1))

print('Obrigado por utilizar a nossa calculadora')