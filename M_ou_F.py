
a = 0

while a < 2 or a > 3:
    print('\nQual o seu sexo?')
    print('[2] Masculino')
    print('[3] Feminino\n')
    a= int(input('Digite aqui a sua opção : '))

if a == 2:
    print('\nConfirmando: Masculino\n')

elif a == 3:
    print('\nConfirmando: Feminino\n')

print('Obrigado pelo seu cadastro!\n')