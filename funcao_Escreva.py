
def escreva (texto):        # Define função escreva chamando mensagem para texto
    tamanho = len (texto)   # Verifica o tamanho da mensagem em quantidade de caracteres

    print ('-' * tamanho)   # exibe "-" n vezes determinada na linha anterior
    print (texto)           # exibe a mensagem digitada
    print ('-' * tamanho)   # repete o primeiro print

# Programa Principal

txt = input('Digite aqui o seu texto : ') # Solicita a digitação da mensagem

a = escreva (txt)  # chama a função escreva para a mensagem txt