altura = input('Digite a sua altura : ')
sexo = input ('Digite m para sexo masculino ou f para feminino : ')

alt = eval (altura)

if sexo == 'm':
    peso = (72.7 * alt) - 58

else:
    peso = (62.1 * alt) - 44.7

print ('O seu peso ideal é {:.2f}'.format(peso))



