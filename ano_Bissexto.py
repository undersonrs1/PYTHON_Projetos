ano = int(input('\nDigite o ano e direi se ele é ou não bissexto : '))
if ano % 4 == 0:
    print('\nO ano de {} é sim um ano bissexto!\n'.format(ano))
else:
    print('\nO ano de {} não é um ano bissexto!\n'.format(ano))
        