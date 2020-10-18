a = [1,2,3,4,5]

b = a

b[0] = 0

print('\nAs listas não se alteram, pois são colocadas em igualdade!')
print('\na : {}'.format (a))
print('b : {}'.format (b))

b = a[:]

b[0] = 1

print('\nNeste segundo caso, as listas ficam diferentes, pois b recebe apenas uma cópia dos itens de a em [:]')
print('\na : {}'.format (a))
print('b : {}'.format (b), end="\n\n")

print('O menor numero em a é {} e o maior é {}'.format(min(a),max(a)))
print('\nO menor numero em b é {} e o maior é {}'.format(min(b),max(b)))