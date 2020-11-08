def busca_binaria(l, x, ini, fim):
    meio = (ini + fim) // 2
    if x == l[meio]:
        return meio
    if x < l[meio]:
        return busca_binaria(l, x, ini, meio - 1)

    if x > l[meio]:
        return busca_binaria(l, x, meio + 1, fim)

import random

a = random.sample(range(100),20)
a.sort()
print()
print(a)
print()
b = str(input('Qual o elemento do vetor que deseja saber o índice? : '))
print()
c = eval(b)

d = busca_binaria(a,c,0,19)

print(d)
print()



 

