lista = list()
cont = 0

while True:
    ins = int(input('\nQual o valor a ser inserido na lista? : '))

    if ins not in lista:
        lista.append(ins)
        resp = str(input('Número adicionado com sucesso! Deseja Continuar (S / N)? : '))
        if resp == 's':
            cont += 1

        if resp == 'n' or cont == 10:
            break

    if ins in lista:
        cont = cont
        
lista.sort()

for c, d in enumerate (lista):
    print('No índice {} está o número {}'.format(c,d))

print(lista)


