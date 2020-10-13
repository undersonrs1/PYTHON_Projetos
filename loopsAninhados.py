str_list = ['Roberto','Joao','Rafael'] # cria lista str_list - lista de strings

for nome in str_list: # criação do for para verificar nomes em str_list

    for c in nome: # associa cada nome contida em str_list a uma variavel c

        if c in 'aeiou': # cada variavel associada a c sera verificado conteudo de vogais e caso positivo imprime

            print(c) # imprime a vogal encontrada no passo anterior

            

