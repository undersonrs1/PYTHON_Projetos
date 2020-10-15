import random
r = random.randint(0,5)
chute = int(input('Tente acertar um número entre 0 e 5 que pensei : '))
if chute == r:
    print('Você acertou! eu havia pensado neste mesmo número!')
else:
    print('Não foi desta vez! Não havia pensado no mesmo número que você!')
    print('Eu havia pensado no número {}!'.format(r))



