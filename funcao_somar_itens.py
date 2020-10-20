def somar(a, b):
    v1 = a
    v2 = b
    s = v1 + v2
    
    print('O resultado da soma entre {} e {} é igual a {}'.format(v1,  v2, s))

# Programa Principal

n1 = int (input('\nDigite o primeiro valor : '))
n2 = int (input('\nDigite o segundo valor : '))

res = somar(n1, n2)
