
def  potencia (base , expoente ):
    resultado = base ** expoente
    return resultado

b = float (  input ( "\nEntre com uma base :  " )  )
exp = float (  input ( "\nEntre com um expoente :  " )  )

pot = potencia (b ,  exp )
print ( "\nResultado  de " , b ,  " elevado  a " ,  exp ,  " :  " ,  pot, end='\n\n' )
