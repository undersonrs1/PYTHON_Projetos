Linha_Origem = 0
Linha_Destino = 0

ferMov = [['Torquimetro',10,'Multimetro',10,'Parafusadeira',10],['Torquimetro',10,'Multimetro',10,'Parafusadeira',10],
['Torquimetro',10,'Multimetro',10,'Parafusadeira',10],['Torquimetro',10,'Multimetro',10,'Parafusadeira',10],
['Torquimetro',10,'Multimetro',10,'Parafusadeira',10]]



print('0-Cpr 1-Cpl 2-Vbe 3-Ggr 4-Sta')
Origem = eval(input('Qual a estação Origem? : '))

while Origem <1 or Origem >5:
    print('0-Cpr 1-Cpl 2-Vbe 2-Ggr 4-Sta')
    Origem = eval(input('Qual a estação Origem? : '))

Destino = eval(input('Qual a estação Destino? : '))

while Destino <1 or Destino >5:
    print('0-Cpr 1-Cpl 2-Vbe 3-Ggr 4-Sta')
    Destino = eval(input('Qual a estação Destino? : '))

Linha_Origem = Origem
Linha_Destino = Destino


print('0-Torquimetro 2-Multimetro 4-Parafusadeira')
Ferramenta = eval(input('Indique a ferramenta : '))

while Ferramenta % 2 != 0 or Ferramenta > 6:
    print('0-Torquimetro 2-Multimetro 4-Parafusadeira')
    Ferramenta = eval(input('Indique a ferramenta : '))

quantOrigem_Ant = (ferMov [Linha_Origem][Ferramenta+1])

quantDestino_Ant = (ferMov [Linha_Destino][Ferramenta+1])

Remove = (ferMov [Linha_Origem][Ferramenta+1]) - 1
ferMov [Linha_Origem][Ferramenta+1] = Remove

Adiciona = (ferMov[Linha_Destino][Ferramenta+1]) + 1
ferMov [Linha_Destino][Ferramenta+1] = Adiciona

ferMov = ferMov

print ('A ferramenta selecionada foi : ')
print (Ferramenta)

print('A estação Origem selecionada foi : ')
print(Origem)

print('A estação Destino selecionada foi : ')
print(Destino)

print('A quantidade desta ferramenta na origem era : ')
print(quantOrigem_Ant)

print('A quantidade desta ferramenta na origem agora é : ')
print(Remove)

print('A quantidade desta ferramenta no destino era : ')
print(quantDestino_Ant)

print('A quantidade desta ferramenta no destino passou a ser : ')
print(Adiciona)












