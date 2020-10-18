import random
sel = 0

while True:
    sel = int(input('\nEscolha ÌMPAR (1) ou PAR (2) : '))
    r = random.randint(1,2)

    if sel == 2 and r % 2 == 0:
        print('\nResultado é PAR!')
        print('\nVocê Venceu')
        print('Você escolheu par e eu ímpar!')
           
    if sel == 1 and r % 2 != 0:
        print('\nResultado é ìMPAR!')
        print ('\nVocê Venceu!')
        print('\nVocê escolheu ímpar e eu par!')
    
    if  sel == 2 and r % 2 != 0:
        print('\nResultado é ÌMPAR!')
        print('\nDesta vez eu venci!')
        print('\nVocê escolheu par e eu ímpar!')
        print('\nJogo encerrado!')
        break

    if sel == 1 and r % 2 == 0:
        print('\nDesta vez eu venci!')
        print('\nResultado é PAR!')
        print('\nVocê escolheu ìmpar e eu par!')
        print('\nJogo encerrado!')
        break


print('\nObrigado por jogar comigo!!!\n')


