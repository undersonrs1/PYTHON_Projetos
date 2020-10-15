tab = int(input('\nDigite qual o valor da tabuada que deseja ver : '))
for a in range (1,11):
    result = a*tab
    print('{} X {} = {}'.format(tab,a,result))
print()