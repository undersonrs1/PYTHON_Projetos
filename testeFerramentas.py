lista = [['GGR','torquimetro',1,'alicate',2,'multimetro',3],['CPR','torquimetro',4,'alicate',5,'multimetro',6]]

ferramenta = input('Qual a ferramenta desejada? : ')

for a in lista:
    for b in range a:
        if b == ferramenta: