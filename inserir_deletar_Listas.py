lista = ['caneta', 'lapis', 'caderno', 'livro'] # cria lista com elementos sala de aula

print (lista) # exibe a lista criada

lista.insert (0,'apontador') # insere na posição 0 o item apontador

print (lista) # exibe novamente a lista

lista.append('borracha') # insere na última posição o item borracha

print (lista) # exibe novamente a lista

lista[2] = 'sulfite' # substitui o item da posição 2 por sulfite

print (lista) # exibe novamente a lista

del lista [0] # deleta o item 0 da lista *** atenção ao uso de colchetes no comando del ***

lista.pop (0)  # deleta o item 0 da lista *** atenção ao uso de parênteses no comando pop ***

print(lista)  # exibe novamente a lista

lista.remove ('borracha')   # remove o item borracha da lista ** no comando remove devemos inserir o  item da lista que desejamos remover

print(lista)  # exibe novamente a lista

# o comando lista.pop() removeria o ultimo elemento da lista
# poderiamos usar também: if caderno in lista: lista.remove ('caderno')

# podemos criar uma lista também utilizando a função range
# valores = list(range(4,11)) =>>>> desta forma criamos uma lista com indices de 0 a 6 e com os valores de 4 a 11 ja armazenados nesta lista

# para ordenarmos uma lista podemos usar o sort. EX: lista.sort()
# para ordenar em ordem inversa: lista.sort(reverse=True)

# len(lista) nos da quantos elementos tem uma determinada lista

# importante lembrar que SEMPRE QUE IGUALAMOS LISTAS ELAS SEMPRE TERÃO OS MESMOS VALORES MESMO QUE ALTEREMOS POSIÇÕES INTERMEDIÁRIAS
# PARA CÓPIA DE A DENTRO DE B POR EXEMPLO FARIAMOS: B = A[:]
