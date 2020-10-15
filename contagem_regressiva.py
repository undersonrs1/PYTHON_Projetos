
import time #importa o módulo do contador de tempo 

for regressiva in range (10, -1, -1): # especifica valor inicial, final e sua iteração
    print(regressiva) # exibe a contagem regressiva
    a = time.time() # marca o inicio da contagem de tempo
    time.sleep(1) # aguarda 1 segundo e prossegue a contagem regressiva

print ('\nContagem regressiva concluída!\n')


