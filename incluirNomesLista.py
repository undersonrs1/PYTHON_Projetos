l = [] # cria lista vazia

nome = input('Digite um nome para inserção na listagem : ') # solicita a digitação do nome

while nome != '':
        l.append(nome) # memoriza o nome na lista l

        nome = input('Digite um nome para inserção na listagem : ') # enquanto nome não é vazio, solicita nome
    
for i in l: # conta i até o tamanho de l
    
    print (i) # imprime todos os elementos de l um abaixo do outro


