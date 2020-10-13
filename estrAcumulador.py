
acum = 0 # cria acumulador acum com valor inicial de 0

for x in range(0,101): # cria for com range variando entre 0 e 101

    if x%2 == 0: # se divisao do numero encontrado por 2 tiver resto 0 prossegue

        acum=acum + x # soma valor testado no passo anterior ao conteudo de acum

print (acum) # exibe valor acumulado total em acum




