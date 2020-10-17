
dist = float(input('\nQuantos kilometros terá a sua viagem? : '))

if dist >= 200:
    preco1 = dist * 0.45
    print('\nSua viagem tem o custo reduzido de R$ 0,45 por km e custará R$ {:.2f} reais \n'.format(preco1))

else:
    preco2 = dist * 0.50
    print('\nSua viagem tem o custo normal de R$ 0,50 por km e custará R$ {:.2f} reais \n'.format(preco2))
    
print('Obrigado por utilizar nossos serviços de cálculo! Boa viagem \n')
