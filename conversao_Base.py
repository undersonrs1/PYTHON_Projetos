
num = eval(input('\nDigite um número inteiro: '))
print('''\nDeseja converter para que tipo de base?

[1] - Binário 
[2] - Hexadecimal
[3] - Octal  

Selecione uma das opções ''')

res = int(input('Digite aqui a opção desejada : '))

if res <1 or res >3:
    print('A opção que selecionou é inválida')
    res = int(input('Digite novamente a opção desejada : '))

elif res == 1:
    print('\nO número {} em binário é = {}'.format(num , bin(num)[2:]))

elif res==2:
    print('\nO número {} em hexadecimal é = {}'.format(num , hex(num)[2:]))

elif res==3:
    print('\nO número {} em octal é = {}'.format(num , oct(num)[2:]))   

print('\nObrigado por utilizar o nosso conversor de bases numéricas!\n\n')
