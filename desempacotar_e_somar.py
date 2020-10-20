def soma ( * read ): # define uma função soma onde os dados serão desempacotados em read
    s = 0 # define variável s recebendo valor 0

    for cada in read: # para cada dado lido em desempacotamento de read
        s += cada     # adicionar esse dado lido á variável s

    print(s) # exibir a somatória dos valores desempacotados que estão contidos em s

soma(2,2)   # tupla 1
soma(3,2,1) # tupla 2


