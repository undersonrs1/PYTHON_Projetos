media1 = float(input('Digite a sua primeira nota : '))
media2 = float(input('Digite a sua segunda nota : '))
mf = (media1+media2)/2
print('Sua média final foi {:.1f}'.format(mf))
if mf >=6:
    print('Parabéns a sua média foi excelente!')
else:
    print('A sua média foi péssima! Estude mais!')

print('------FIM---------')