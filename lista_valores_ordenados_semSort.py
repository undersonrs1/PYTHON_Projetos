lista_1 = []
lista_2 = []
count = 0

for a in range(0,5):

    b = int(input('Digite o valor a ser acrescentado á lista : '))

    lista_1.append(b)
    count +=1

d = (len(lista_1)-1)

if lista_1[0] > lista_1[1]:
        print ('{} e {}'.format(lista_1[0],lista_1[1]))

        lista_2[0] = lista_1[1]
        lista_2[1] = lista_1[0]
        
        print ('{} e {}'.format(lista_2[0],lista_2[1]))



print (lista_1)
print (lista_2)
