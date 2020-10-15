termo1 = int (input('\nDigite o primeiro termo da progressão aritmética : '))

termo2 = int (input('\nDigite o termo final da progressão aritmética : '))

r = int (input('\nDigite qual a razão desta progressão aritmética : '))

i = termo1 + r

for a in range (i, termo2, r):

    print (a, end=" ")
