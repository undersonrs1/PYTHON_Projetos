num = 0
while True:
    num = int(input('Deseja calcular a tabuada de que valor? : '))
    if num < 0:
        break
    for a in range (0,11):
        mult = num * a
        print('{} X {} = {}'.format(num,a,mult))

print('Tabuada interrompida pelo usuário!')



