
def contador(inicio, fim, incremento):
    for a in range (inicio, fim, incremento):
        print (a, end=' ')

# Programa Principal

i = int (input('\nDigite o número inicial de sua contagem : '))
f = int (input('\nDigite o número final de sua contagem : '))
inc = int (input('\nDigite o incremento de sua contagem : '))

cont = contador (i, f, inc)

